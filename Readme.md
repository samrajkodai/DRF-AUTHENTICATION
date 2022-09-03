# DJANGO REST AUTHENTICATION with DJOSER


[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

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

## Installation

Django Rest Frame_work requires


Install the dependencies by using the following command.

```sh
pip install djangorestframework
```

add the frame work in settings file...

```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'API',
    'rest_framework',
    'rest_framework_swagger',
]
```

## Server

for start the django server use the following command

```sh
python manage.py runserver
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
