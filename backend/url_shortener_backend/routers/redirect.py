from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse, RedirectResponse
from sqlmodel import Session

from url_shortener_backend import crud
from url_shortener_backend.database import get_session

router = APIRouter()

@router.get("/")
def index():
    return FileResponse("static/index.html")

@router.get("/health-check")
def health_check():
    return {"status": "ok"}

@router.get("/{code}")
def redirect(code: str, session: Session = Depends(get_session)):
    url = crud.get_url(session, code)
    if url is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Url not found"
        )
    else:
        return RedirectResponse(url=url.original_url, status_code=302)