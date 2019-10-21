#!/bin/bash

# drop otsukai database
mysql -uroot -proot -e 'drop database otsukai;'
mysql -uroot -proot -e 'create database otsukai;'

# clear previous migration files
rm -rf otsukai/migrations/*
rm -rf errand/migrations/*
rm -rf accounts/migrations/*

# make each app migration files
python manage.py makemigrations otsukai
python manage.py makemigrations accounts
python manage.py makemigrations errand

# migrate
python manage.py migrate

# loaddata
python manage.py loaddata initial_category
python manage.py loaddata initial_user
python manage.py loaddata initial_errand

exit 0
