# Overview
This is an app that requests errand.

# System Diagram
![](https://otsukai.s3-ap-northeast-1.amazonaws.com/otsukai_diagram.png)

# Description
## apps
- accounts  
management users.
    - register, login, logout

- errand  
request errand functions.  
    - select partners
    - send mail users and partners

- mail  
send email to user when receive errand, and send notification to slack.  
**Note**: This is mock app so send it to dango-team of ITProjectPromotion which is a test workspace.

- prediction  
enter your rank and capacity, returns your future s\*l\*r\*!

## heroku
access [here](https://fathomless-mesa-47202.herokuapp.com/)


# Requirement
## python library
```bash
pip install -r requirements.txt
```

## Usage

run server
```bash
python manage.py runserver 0.0.0.0:8000
```

create database tables
```bash
python manage.py migrate
```

load initial data
```bash
python manage.py loaddata initial_user.json
```

if you send mail test, set your gmail accoutn info in `setting.py`.
```python setting.py
EMAIL_HOST_USER = ''  # set your gmail address
EMAIL_HOST_PASSWORD = ''  # set your gmail password
```
