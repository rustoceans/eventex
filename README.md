EventeX
=======

Sistema para controle de eventos desenvolvido no curso Welcome to the Django 14.

A aplicação está hospedada no Heroku e pode ser visualizada [aqui.](http://eventex-matheus.herokuapp.com/)

#### Download and Run:

    git clone https://github.com/matheusho/eventex.git
    cd eventex
    pip install -r requirements.txt

### Env ###

Criar arquivo .env com a Secret Key e o modo DEBUG:

    touch .env

    -- Content file
    SECRET_KEY='YOUR-SECRET-KEY'
    DEBUG=True

### Syncdb ###
    python manage.py syncdb --migrate

### Para rodar o projeto: ###

    python manage.py runserver
