FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml /app/

RUN poetry lock --no-interaction

COPY alembic.ini /app/

RUN poetry install --no-root --no-interaction

COPY app /app/app

CMD ["poetry", "run", "fastapi", "run", "app/main.py", "--proxy-headers", "--port", "80"]
