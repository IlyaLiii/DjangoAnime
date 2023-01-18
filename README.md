Разворачивание проекта на Debian

1) Клонировать проект
2) Создать виртуальное окружение в корне проекта
3) Установить пакеты из requirements.txt командой:
    pip install -r requirements.txt

Ошибка Error: pg_config executable not found.

sudo apt-get install libpq-dev python3-dev -y

Ошибка error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1

sudo apt-get install python3-dev python3-setuptools
sudo apt-get install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

4) Поставить файл локального конфига env.env (Взять у главного разработчика)
5) Развернуть postgres локально:
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    sudo systemctl start postgresql.service

    sudo -u postgres createuser --interactive
    (Назвать юзера Mori)

    sudo -i -u postgres
    sudo -u postgres createdb Mori

    sudo adduser Mori --force-badname
    sudo -i -u Mori
    psql

    \conninfo
    (В output должно быть: You are connected to database "Mori" as user "Mori" via socket in "/var/run/postgresql" at port "5432".)

    Найти файл конфига pg_hub.conf и поставить метод trust

6) Провести миграции:
    python manage.py makemigrations
    python manage.py migrate

7) Создать суперпользователя:
    python manage.py createsuperuser

8) Запустить скрипт parce_for_postgress.py для заполнения DB


