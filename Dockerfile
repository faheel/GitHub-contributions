FROM python:3.7-alpine

RUN apk add curl jq

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN python3 -m venv /venv/bin/python3
RUN pip install -r requirements.txt