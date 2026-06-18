from sqlmodel import create_engine, Session
from url_shortener_backend.config import app_config

engine = create_engine(app_config.DATABASE_URL, pool_pre_ping=True, pool_size=10, max_overflow=20, pool_timeout=30)

def get_session():
    with Session(engine) as session:
        yield session
