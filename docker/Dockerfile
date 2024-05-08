FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./app /app

RUN pip install SQLAlchemy asyncpg

EXPOSE 8000
