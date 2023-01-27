FROM python:3.9-slim

COPY . /api
WORKDIR /api

RUN apt update -y && apt-get install -y libpq5 libpq-dev
RUN apt install -y python3-pip
RUN python3 -m pip install -r requirements.txt
