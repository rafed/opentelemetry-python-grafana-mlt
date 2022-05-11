FROM python:3.8-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /webapp

COPY requirements.txt /webapp
RUN pip install -r requirements.txt

COPY webapp/ /webapp/
