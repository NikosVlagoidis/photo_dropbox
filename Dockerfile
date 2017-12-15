FROM python:3.5-slim

MAINTAINER Nikos Vlagoidis

EXPOSE 5000

CMD ["./bin/run-prod.sh"]

WORKDIR /app


RUN adduser --uid 1000 --disabled-password --gecos '' --no-create-home deploy

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -f /var/cache/apt/archives/*.deb && \
    rm -rf /var/lib/apt/list/*

RUN pip install --no-cache-dir uwsgi

COPY requirements.txt /app/requirements/prod.txt
RUN pip install --no-cache-dir -r /app/requirements/prod.txt

COPY . /app

RUN chown deploy.deploy -R /app

RUN chmod 755 ./bin/run-prod.sh

USER deploy
