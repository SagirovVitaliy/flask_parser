FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential

ADD requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /flask_parser
ADD . /flask_parser

EXPOSE 5000


