FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /flask_parser
ADD . /flask_parser

EXPOSE 5000