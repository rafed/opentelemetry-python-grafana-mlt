FROM python:3.8-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /webapi

COPY requirements.txt /webapi
RUN pip install -r requirements.txt

COPY webapi/ /webapi/
