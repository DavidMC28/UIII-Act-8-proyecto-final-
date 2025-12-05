#!/bin/sh
source .venv/bin/activate
python backend_guarderia/manage.py runserver $PORT
