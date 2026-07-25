#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
if [ ! -d "venv" ]; then
  python -m venv venv
fi
source venv/Scripts/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
