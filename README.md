# URL Shortener

A small URL shortening service. Paste in a long URL, get back a short one that redirects to the original.

Backend is FastAPI + PostgreSQL, frontend is React. The whole thing runs with Docker Compose.

## Running it

```bash
docker compose up
```

Then open http://localhost:8000.

## How it works

Short codes are 7-character random strings (alphanumeric), generated with Python's `secrets` module so they aren't guessable. 

Routes:

- `POST /api/url` — create a short URL
- `GET /api/url/{code}` — look up where a code points
- `GET /{code}` — redirect (302)

## Local development

Backend:

```bash
cd backend
poetry install
poetry run start
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

The Vite dev server proxies `/api` to the backend, so you just hit http://localhost:5173.

You'll need a Postgres instance running and a `DATABASE_URL` set — see `.env.example`.

## Tests

```bash
cd backend
poetry run pytest
```
