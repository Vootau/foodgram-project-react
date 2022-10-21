![Build Status](https://github.com/Vootau/foodgram-project-react/actions/workflows/main.yml/badge.svg)

#### stack

![Python](https://img.shields.io/badge/Python-3.7.0-blue?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/Django-3.2.15-orange?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Edge](https://img.shields.io/badge/Edge-0078D7?style=for-the-badge&logo=Microsoft-edge&logoColor=white)

### What is about

Project foodgram allow you to watch, create recipes
subscribe on users (except yourself)
and download shopping list of ingedients.

### After push command into git repository

1. PEP8 check (with Flake8)
2. Build and push images to dockerhub
3. Deploy to remote server
4. Sending message to Telegram if success

### How to start project

Clone repo and go to directory in command line:

```
git clone https://github.com/Vootau/foodgram-project-react.git
```

```
cd backend
```

Create and activate virtual environment:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Install dependences from requirements.txt:

```
pip install -r requirements.txt
```

Make migrations:

```
python manage.py migrate
```

Upload ingerdients and tags from .csv files (if nesessary):

```
python manage.py import csv
```

Run project:

```
python manage.py createsuperuser

python manage.py runserver
```

Server_ip:

```
130.193.54.202

Api documentation:
http://130.193.54.202/api/docss/

Unauthorized access:
http://130.193.54.202/api/users/
http://130.193.54.202/api/recipes/
http://130.193.54.202/api/ingredients/

Register:
http://130.193.54.202/api/users/ [Method: POST]

Sign in:
http://130.193.54.202/api/auth/token/login

Admin:
http://130.193.54.202/admin/

login : admin
pswd : qxezwc123
