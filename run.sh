#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn meta_id.wsgi:application -w 2 -b :8000
