# ---- build frontend ----
FROM node:20-alpine AS frontend
WORKDIR /fe
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# ---- python runtime ----
FROM python:3.12-slim
WORKDIR /app/backend

RUN pip install --no-cache-dir poetry==2.4.1
RUN poetry config virtualenvs.create false

COPY backend/pyproject.toml backend/poetry.lock ./
RUN poetry install --only main --no-interaction --no-ansi

COPY backend/ ./
COPY --from=frontend /fe/dist ./static
CMD uvicorn url_shortener_backend.app:app --host 0.0.0.0 --port 8000