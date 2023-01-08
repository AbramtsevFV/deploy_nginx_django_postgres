#!/usr/bin/env bash
set -e

python manage.py migrate

mkdir -p /data/public

python manage.py runserver --settings=photo.settings 0.0.0.0:8000
