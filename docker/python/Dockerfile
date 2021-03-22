FROM python:3.8-buster as develop

ENV POETRY_VERSION=1.1.* \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt install -y \
       gcc \
       make \
    && pip install \
       "poetry==$POETRY_VERSION" \
       fastapi \
       asyncpg \
       aiosql \
       PyJWT \
       pytest \
       memory-profiler

FROM develop as build

WORKDIR /api
COPY . /api

RUN poetry config virtualenvs.create false \
    && poetry export -f requirements.txt | pip install -r /dev/stdin \
    && poetry build

FROM python:3.8-slim as final

COPY --from=build /api/dist /api/dist
COPY --from=build /api/app /api/app
COPY --from=build /api/gunicorn_config.py /api/gunicorn_config.py

RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn /api/dist/*.whl

ENTRYPOINT ["/usr/local/bin/gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/api/gunicorn_config.py", "app.main:app"]
