FROM python:3.10-slim as service_1_builder

ARG ENV_FILE

WORKDIR /app_1/service_1

RUN apk update && apk add curl && \
    apk add bash && apk add --no-cache ffmpeg ffmpeg-libs && \
    curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PYTHONPATH="${PYTHONPATH}:/service_1"

COPY $ENV_FILE /service_1/pyproject.toml /service_1/poetry.lock service_1/ ./

RUN bash -c "poetry install --no-root --only main"


FROM service_1_builder as service_2_builder

WORKDIR /app_2/service_2

# В этой строке не ошибка, нужны зависимости от сервиса 1 :)
COPY $ENV_FILE /service_1/pyproject.toml /service_1/poetry.lock service_2/. ./

ENV PATH="/root/.local/bin:$PATH" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PYTHONPATH="${PYTHONPATH}:/service_2"


FROM python:3.10-slim

WORKDIR /app

COPY --from=service_1_builder /app_1/service_1 /app_1/service_1
COPY --from=service_2_builder /app_2/service_2 /app_2/service_2

EXPOSE 8000
EXPOSE 8001
