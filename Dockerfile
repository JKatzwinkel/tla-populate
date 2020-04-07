FROM python:alpine

ARG SAMPLE_URL

COPY . /app

WORKDIR /app

RUN apk upgrade --no-cache \
    && apk add tar wget \
    && wget -q "${SAMPLE_URL}" -O sample.tar.gz \
    && tar -xzf sample.tar.gz \
    && rm sample.tar.gz \
    && pip install --no-use-pep517 . \
    && echo "start ingestion script" \
    && tla-populate-backend
