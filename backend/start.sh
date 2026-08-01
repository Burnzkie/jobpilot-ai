#!/bin/sh

echo "Running database migrations..."

alembic upgrade head

echo "Starting JobPilot AI..."

exec uvicorn main:app \
    --host 0.0.0.0 \
    --port ${PORT:-8000}