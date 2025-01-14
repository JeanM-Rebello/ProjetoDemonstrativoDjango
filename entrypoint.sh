#!/bin/sh

echo "Ajustando permissões do diretório /django_project/staticfiles"
mkdir -p /django_project/staticfiles
chown -R appuser:appuser /django_project

until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  echo "🟡 Esperando Disponibilidade do Banco para Conexão ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Conexão no Banco Realizada com Sucesso ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver 0.0.0.0:8000