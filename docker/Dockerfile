FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry install --no-root --no-interaction

COPY app /app/app

CMD ["poetry", "run", "fastapi", "run", "app/main.py", "--proxy-headers", "--port", "80"]
