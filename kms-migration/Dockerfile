FROM python:3.11-rc-alpine

WORKDIR /app

COPY app.py /app
COPY .env /app
COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

