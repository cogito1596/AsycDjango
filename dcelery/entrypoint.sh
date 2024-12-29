#!/bin/ash

echo "Applying Database migrations"
python manage.py migrate

exec "$@"