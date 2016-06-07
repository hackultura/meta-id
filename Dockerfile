FROM python:3.5

RUN apt-get update -y
RUN apt-get install -y mercurial

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY . /usr/src/app

RUN pip install -r requirements.txt
