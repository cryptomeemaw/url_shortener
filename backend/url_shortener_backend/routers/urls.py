from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from starlette import status

from url_shortener_backend import crud
from url_shortener_backend.config import app_config
from url_shortener_backend.database import get_session
from url_shortener_backend.schemas import URLCreate, URLRead

router = APIRouter()


@router.post("/url", response_model=URLRead, status_code=status.HTTP_201_CREATED)
def create_url(payload: URLCreate, session: Session = Depends(get_session)):
    short_url = crud.create_short_url(session, str(payload.url))
    if short_url is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not generate a unique short code, please try again",
        )
    return URLRead(
        code=short_url.short_code,
        original_url=short_url.original_url,
        short_url=f"{app_config.BASE_URL}/{short_url.short_code}",
    )


@router.get("/url/{code}", response_model=URLRead)
def get_url(code: str, session: Session = Depends(get_session)):
    url = crud.get_url(session, code)
    if url is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Url not found"
        )
    else:
        return URLRead(
            code=url.short_code,
            original_url=url.original_url,
            short_url=f"{app_config.BASE_URL}/{url.short_code}",
        )
