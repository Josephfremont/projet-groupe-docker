#!/bin/sh

# Apply database migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser --noinput || true # Uses DJANGO_SUPERUSER_<var> environment variables

# Generate token for superuser and filter out the token
TOKEN=$(python manage.py drf_create_token admin | awk '/Generated token/ {print $3}')

# Export token as environment variable
export API_TOKEN=$TOKEN

# Load initial data
python manage.py loaddata fixtures.json

# Start the Django server
exec python manage.py runserver 0.0.0.0:8000
