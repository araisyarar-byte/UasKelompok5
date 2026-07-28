#!/usr/bin/env bash
set -e
python -m venv .venv
source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py isi_demo
python manage.py runserver
