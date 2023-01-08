FROM python:3.8
ENV PYTHONUNBUFFERED 1

COPY ./photo_load /srv/www/photo_load
WORKDIR /srv/www/photo_load
RUN pip install -r requirements.txt
