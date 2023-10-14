#!/usr/bin/env bash

git pull master master

pip install -r requirements.txt

python manage.py collectstatic
python manage.py migrate