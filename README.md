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

### development

    ./bin/develop

for dev mode.

### production

Yelo is a Django app, so you can really choose whatever gateway interface you want.

But, if you don't have a preference, we chose gunicorn.

You can start a production gunicorn server with:

    ./bin/production

(you can modify uranium.yaml to change the settings)

`note`: on the production server, statics have to be served separately.
See the host_config/yelo.conf for an example of how to do this with nginx.

Remember, you have to collect statics with django:

    ./bin/python manage.py collectstatic
