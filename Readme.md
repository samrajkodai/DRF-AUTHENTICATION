# DJANGO REST AUTHENTICATION with DJOSER


[![N|Solid](https://user-images.githubusercontent.com/61903698/188264476-cd5f36d4-04ac-4198-842b-c5d1f1ecd3fd.png)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This project is about make an authentication with Django Rest Framework token with Djoser.

## Djoser Installation and setup
Djoser is a Package that hepls to make a authentication easier. 

To learn more about djoser please visit https://djoser.readthedocs.io/en/latest/

## Database 

This project is connected with mysql Database for connecting mySQL Database using this following configurations
```sh
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'yor_database',  
        'USER': 'root',  
        'PASSWORD': 'your_password',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}  
```
### step 1
Install the dependencies by using the following command.


```sh
pip install -r requirements.txt
```

### step 2

Add the djoser and rest_framework in setting.py file

```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authapp',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken'
]
```
### step 3

and also add the djoser in urls.py file
```sh
    path('',include("djoser.urls")),
    path('',include('djoser.urls.authtoken'))
```
### step 4
make migrations and run the server

```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```

### step 5

visit the following urls it's works

- http://127.0.0.1:8000/users/
- http://127.0.0.1:8000/token/login


### signup
![Screenshot_1](https://user-images.githubusercontent.com/61903698/188263952-b633b7c4-407d-4b07-bb3c-588c94d57059.png)

### Login
![Screenshot_2](https://user-images.githubusercontent.com/61903698/188264004-22a1b86d-9d89-47ef-8c14-1757fbdbdf2c.png)

### Token

![Screenshot_3](https://user-images.githubusercontent.com/61903698/188264036-d0bfc9b7-7bf8-4e49-aeda-04cbdb9392c7.png)



## License

MIT
