FROM python:3.12.2

ENV PYTHONUNBUFFERED 1

WORKDIR /django_app/

COPY requirements.txt /django_app/

RUN pip install -r requirements.txt

COPY . .


