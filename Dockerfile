FROM python:alpine

ARG SAMPLE_URL
ARG BACKEND_URL

COPY . /app

WORKDIR /app

ENV BACKEND_URL ${BACKEND_URL}

ENTRYPOINT ["tla-populate-backend", "${BACKEND_URL}"]

RUN apk upgrade --no-cache \
    && apk add tar wget \
    && echo "download corpus data from ${SAMPLE_URL}..." \
    && wget -q "${SAMPLE_URL}" -O sample.tar.gz \
    && tar -xzf sample.tar.gz \
    && rm sample.tar.gz \
    && pip install --no-use-pep517 .

