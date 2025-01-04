# brandquad_backend_test_task

Ссылка на тестовое задание - https://drive.google.com/file/d/1-grxFjcca7LZS2LlXJUZ_SaTOUMZucgn/view?usp=drive_link

# Стек

- Python 3.12.7
- Django 5.1.4
- Django REST framework 3.15.2

# Справка

Для простоты приложение запускается на dev сервере (для задания это некритично), посему DEBUG=False, чтобы Django раздавал статические файлы для админки.

Документация доступна по следующий эндпоинтам:

Swagger:
```
/api/v1/swagger/
```

Redoc:
```
/api/v1/redoc/
```

# Запуск

### 1) Запуск на сервере разработчика Django:

**Первоочередно, конечно, необходимо создать и активировать виртуальное окружение, а затем установить зависимости:**

Виртуальное окружение:

Windows:

```bash
py -3 -m venv env
```

```bash
. venv/Scripts/activate 
```

macOS/Linux:

```bash
python3 -m venv .venv
```

```bash
source env/bin/activate
```

Зависимости:

```bash
pip install -r requirements.txt
```

**Вторым шагам следует осуществить миграции:**

Windows: 

```bash
py manage.py makemigrations
```

```bash
py manage.py migrate
```

macOS/Linux:

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

**Сам проект запускается стандартно с помощью команды:**

Windows:

```bash
py manage.py runserver
```
Linux/MacOS

```bash
python3 manage.py runserver
```

**Для доступа в Django админку необходимо создать суперпользователя:**

Windows:

```bash
py manage.py createsuperuser
```
Linux/MacOS

```bash
python3 manage.py createsuperuser
```

**Запуск management команды для загрузки логов:**

Windows:

```bash
py manage.py parse_logs <url>
```

Linux/MacOS

```bash
python3 manage.py parse_logs <url>
```

**Запуск тестов:**

```bash
py manage.py test
```

Linux/MacOS

```bash
python3 manage.py test
```

### 2) Запуск на Docker контейнерах:

Для запуска проекта используется 2 контейнера: postgres - база данных PostgreSQL, bq-logs-django - Django приложение.

Чтобы "поднять" контейнеры нужно перейти в директорию с docker-compose файлом и ввести в терминал следующую команду:

```bash
docker compose up -d --build
```

При запуске в контейнерах сборка создание миграций и их применение, запуск management команды на загрузку логов и создание суперпользователя автоматизированы.

**Данные для входа в админку:**

Login - admin

Password - admin

E-mail - admin@gmail.com

