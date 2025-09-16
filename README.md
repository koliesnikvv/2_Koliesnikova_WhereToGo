Where to go?

to work with this project clone repository

git clone <your-repository>

cd favouritePlaces

python -m venv venv

venv\Script\activate

then you need to install requirements

pip install -r requirements.txt

python manage.py migrate

load data

python manage.py loaddata myplaces.json

python manage.py createsuperuser

then run server

python manage.py runserver

you'll open this link http://127.0.0.1:8000/ and after that you can work with site and get a random place to go
