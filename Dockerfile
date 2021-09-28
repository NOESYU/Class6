FROM python:3.9.0

WORKDIR /home/

RUN echo "dsfwfsdfas"

RUN git clone https://github.com/NOESYU/django.git

WORKDIR /home/django/

# 이제 필요없음 ~
# RUN echo "SECRET_KEY=django-insecure-&7&6%y_u!llubrd*8erq&m8mogj!x5(*(13rc(+lb5ks(b2ckv" > .env
RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c","python manage.py collectstatic --noinput --settings=django_0629.settings.deploy && python manage.py migrate --settings=django_0629.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=django_0629.settings.deploy django_0629.wsgi --bind 0.0.0.0:8000"]
