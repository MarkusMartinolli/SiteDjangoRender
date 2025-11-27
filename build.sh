#!/bin/bash
# Build script para Render

set -o errexit

# Instalar dependências
pip install -r requirements.txt

# Executar migrações
python manage.py migrate

# Coletar arquivos estáticos (se necessário)
python manage.py collectstatic --noinput
