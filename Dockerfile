FROM python:3.9-slim

RUN pip install poetry==2.1.2

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry install --no-root --no-interaction

COPY . /app/

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

