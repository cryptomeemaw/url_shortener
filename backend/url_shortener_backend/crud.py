import logging
from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from url_shortener_backend import shortener
from url_shortener_backend.config import app_config
from url_shortener_backend.models import URL

logger = logging.getLogger(__name__)

def create_short_url(session: Session, original_url: str) -> Optional[URL]:
    for attempt in range(10):
        shortened_url = shortener.generate_code(app_config.CODE_LENGTH)
        short_url = URL(
            short_code=shortened_url,
            original_url=original_url,
        )
        try:
            session.add(short_url)
            session.commit()
            session.refresh(short_url)
            return short_url
        except IntegrityError as e:
            logger.info(f"Failed to insert URL row, {shortened_url} already exists, retrying...: {e}")
            session.rollback()
    logger.error(f"Failed to insert URL row after 10 attempts")
    return None


def get_url(session: Session, short_code: str) -> Optional[URL]:
    statement = select(URL).where(URL.short_code == short_code)
    result = session.exec(statement).first()
    return result
