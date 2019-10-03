# Overview
This is an app that requests errand.

# Description
## apps
- accounts app  
management users.
    - register, login, logout

- errand app  
request errand functions.  
    - select partners
    - send mail users and partners

## heroku
access [here](https://fathomless-mesa-47202.herokuapp.com/)


# Requirement
## python library
```bash
pip install -r requirements.txt
```

## Usage
- run server
```bash
python manage.py runserver 0.0.0.0:8000
```

- migrate
```bash
python manage.py migrate
```
- load initial data
```bash
python manage.py loaddata initial_user.json
```
