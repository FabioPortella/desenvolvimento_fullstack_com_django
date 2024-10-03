#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install poetry -U
poetry install --no-root --no-dev

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Criando um superuser
# python manage.py createsuperuser --no-input

# Adicionar estas variaves de ambiante
# DJANGO_SUPERUSER_EMAIL
# DJANGO_SUPERUSER_PASSWORD
# DJANGO_SUPERUSER_USERNAME

