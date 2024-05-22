FROM python:3.11.6

WORKDIR /app


COPY pyproject.toml poetry.lock ./


RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi


COPY src/ /app


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
