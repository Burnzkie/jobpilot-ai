#!/bin/sh

if [ "$TESTING" != "true" ]; then
    echo "Running database migrations..."
    alembic upgrade head
fi

echo "Starting JobPilot AI..."

exec uvicorn main:app \
    --host 0.0.0.0 \
    --port ${PORT:-8000}