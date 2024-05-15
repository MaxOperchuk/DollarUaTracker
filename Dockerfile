FROM python:3.11.0-slim
LABEL maintainer="maksym.operchuk@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

ENV PYTHONPATH="/app"

RUN pip install -r requirements.txt

COPY . .