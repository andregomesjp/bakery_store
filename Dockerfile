# syntax=docker/dockerfile:1.2
FROM python:3.8-slim

WORKDIR /usr/src/app

ENV PYTHONPATH=. \
  VENV=/opt/venv

RUN python3 -m venv $VENV
ENV PATH="$VENV/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  ebtables \
  netbase \
  && rm -rf /var/lib/apt/lists/* \
  && update-ca-certificates

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 80
HEALTHCHECK CMD curl --fail http://localhost:80/healthcheck || exit 1

ENV FLASK_ENV=production
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:80"]
