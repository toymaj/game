FROM python:latest

WORKDIR /app

COPY . .

RUN python -m pip install poetry
RUN python -m poetry config virtualenvs.create false && \
    python -m poetry install --no-interaction --no-ansi


CMD echo "[+] Run main" && \
    uvicorn main:app --reload --host 0.0.0.0 --port 8080
