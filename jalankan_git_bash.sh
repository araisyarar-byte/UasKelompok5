#!/usr/bin/env bash
set -e

if [ ! -d "venv" ]; then
  python -m venv venv
fi

source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
