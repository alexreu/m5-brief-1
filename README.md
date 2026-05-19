# Calcul de carre avec FastAPI et Streamlit

Projet individuel MLOps minimal compose d'un frontend Streamlit et d'une API FastAPI. Le frontend envoie un entier au backend, puis l'API retourne son carre apres validation Pydantic.

## Architecture

```text
frontend/
  app.py
  Dockerfile
backend/
  main.py
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

## Routes API

`GET /`
Retourne un message de bienvenue.

`GET /health`
Retourne l'etat de sante de l'API.

`POST /calcul`
Attend un JSON contenant un entier strict, puis retourne son carre.

Exemple de payload :

```json
{
  "nombre": 4
}
```

Exemple de reponse :

```json
{
  "nombre": 4,
  "resultat": 16
}
```

## Lancement avec Docker Compose

```bash
docker compose up --build
```

Services disponibles :

- Frontend Streamlit : `http://localhost:8501`
- Backend FastAPI : `http://localhost:8000`
- Documentation Swagger : `http://localhost:8000/docs`

## Tests backend

Depuis le dossier `backend` :

```bash
pip install fastapi "uvicorn[standard]" pydantic loguru pytest
pytest
```

## Integration continue

Le workflow GitHub Actions `.github/workflows/test.yml` installe les dependances backend et lance `pytest` a chaque `push` et `pull_request`.

## Logs

Les logs applicatifs sont geres avec Loguru dans :

- `backend/main.py` pour les appels aux routes FastAPI
- `frontend/app.py` pour les appels HTTP vers l'API
