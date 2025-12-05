@echo off
echo Starting JSON Server...
start cmd /k "json-server --watch movie_db.json --port 3000"

echo Starting FastAPI Server 1...
start cmd /k "uvicorn user_api:app --reload --port 8001"

echo Starting FastAPI Server 2...
start cmd /k "uvicorn movie_api:app --reload --port 8002"

echo Starting FastAPI Server 3...
start cmd /k "uvicorn genre_api:app --reload --port 8003"

echo Starting FastAPI Server 4...
start cmd /k "uvicorn rating_api:app --reload --port 8004"

echo All servers started.
pause