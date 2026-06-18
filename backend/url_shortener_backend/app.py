import os

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from url_shortener_backend.routers import urls, redirect


def create_app() -> FastAPI:
    url_shortener_app = FastAPI(title="URL Shortener")

    url_shortener_app.include_router(urls.router, prefix="/api")

    # Mount the built frontend assets for use by Docker only created by the Dockerfile
    # Conditional because the directory is absent in local dev, and StaticFiles errors if it's missing
    if os.path.isdir("static/assets"):
        url_shortener_app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")

    url_shortener_app.include_router(redirect.router)

    return url_shortener_app


def main():
    uvicorn.run("url_shortener_backend.app:app", host="0.0.0.0", port=8000, reload=True)


app = create_app()
