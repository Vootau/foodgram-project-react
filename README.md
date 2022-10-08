### What is about

Project foodgram allow you to watch, create recipes
subscribe on users (except yourself)
and download shopping list of ingedients.

### How to start project:

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

Upload ingerdients from .csv file (if nesessary):

```
python manage.py import csv
```

Run project:

```
python manage.py runserver

python manage.py createsuperuser
```

