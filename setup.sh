#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Apply Django migrations
python manage.py migrate

# Collect static files (if needed)
python manage.py collectstatic --noinput
