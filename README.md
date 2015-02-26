# yelo
an elo rating webservice


## setting it up

Yelo needs python 3 or higher. Yelo uses
[uranium](http://uranium.readthedocs.org/en/latest/) to handle
dependencies, so you can bootstrap a service with:

    ./uranium

Next, setup the database with:

    ./bin/python manage.py migrate

(yelo will use a local sqlalchemy by default)

finally, create a superuser:

    ./bin/python manage.py createsuperuser

And you're data is set up!

## running

    ./bin/develop

for dev mode.
