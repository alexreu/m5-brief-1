# Square Calculator with FastAPI and Streamlit

Minimal individual MLOps project composed of a Streamlit frontend and a FastAPI API. The frontend sends an integer to the backend, then the API returns its square after Pydantic validation.

## Architecture

```text
frontend/
  app.py
  Dockerfile
backend/
  main.py
  requirements.txt
  modules/
    calcul.py
  tests/
    test_calcul.py
  Dockerfile
.github/
  workflows/
    test.yml
docker-compose.yml
README.md
```

## API Routes

`GET /`
Returns a welcome message.

`GET /health`
Returns the API health status.

`POST /calcul`
Expects JSON containing a strict integer, then returns its square.

Payload example:

```json
{
  "number": 4
}
```

Response example:

```json
{
  "number": 4,
  "result": 16
}
```

## Run with Docker Compose

```bash
docker compose up --build
```

Available services:

- Frontend Streamlit : `http://localhost:8501`
- Backend FastAPI : `http://localhost:8000`
- Documentation Swagger : `http://localhost:8000/docs`

## Backend Tests

From the `backend` directory:

```bash
pip install -r requirements.txt pytest
pytest
```

## Continuous Integration

The GitHub Actions workflow `.github/workflows/test.yml` installs backend dependencies and runs `pytest` on every `push` and `pull_request`.

## Logs

Application logs are handled with Loguru in:

- `backend/main.py` for FastAPI route calls
- `frontend/app.py` for HTTP calls to the API
