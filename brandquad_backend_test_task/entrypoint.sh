: ${DJANGO_SU_NAME:=admin}
: ${DJANGO_SU_EMAIL:=admin@gmail.com}
: ${DJANGO_SU_PASSWORD:=admin}

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py parse_logs https://drive.google.com/file/d/18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp/view
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SU_NAME', '$DJANGO_SU_EMAIL', '$DJANGO_SU_PASSWORD')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000
