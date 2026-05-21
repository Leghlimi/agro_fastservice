
web: python manage.py migrate --fake contenttypes 0001 && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn agro_fastservice.wsgi --log-file - --bind 0.0.0.0:$PORT