import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool

from url_shortener_backend.app import app
from url_shortener_backend.config import app_config
from url_shortener_backend.database import get_session


@pytest.fixture(name="client")
def db_engine():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)

    def get_session_override():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_session_override
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_create_url_success(client):
    resp = client.post("/api/url", json={"url": "https://google.com/"})
    assert resp.status_code == 201

    data = resp.json()
    assert data["original_url"] == "https://google.com/"
    assert len(data["code"]) == app_config.CODE_LENGTH
    assert data["short_url"].endswith(data["code"])


def test_get_url_returns_original(client):
    created = client.post("/api/url", json={"url": "https://open.gov.sg/"}).json()
    resp = client.get(f"/api/url/{created['code']}")

    assert resp.status_code == 200
    assert resp.json()["original_url"] == created["original_url"]


def test_get_url_missing_returns_404(client):
    resp = client.get("/api/url/doesnotexist")
    assert resp.status_code == 404