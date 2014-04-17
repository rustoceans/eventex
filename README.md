EventeX
=======

Sistema para controle de eventos desenvolvido no curso Welcome to the Django 14.

A aplicação está hospedada no Heroku e pode ser visualizada [aqui.](http://eventex-matheus.herokuapp.com/)

#### Download:

    git clone https://github.com/matheusho/eventex.git
    cd eventex
    pip install -r requirements.txt

### Env

Renomear arquivo rename-as-.env para .env e definir a Secret:

    mv rename-as-.env .env

    -- Content file
    SECRET_KEY={{ SECRET_KEY }} # Set your SECRET KEY here!
    DEBUG=True

### Syncdb ###
    python manage.py syncdb --migrate

#### Run:

    python manage.py runserver
