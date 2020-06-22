> $ terminal command
- repo work
**file location**



initilize repo

**do not migrate until user model is authenticated with admin**

**config/settings.py**
INSTALLED_APPS = ```'users.apps.UsersConfig',```
AUTH_USER_MODEL = ```users.CustomUser```

**users/medels.py**
- create custom user class inheriting AbstractUser

**CREATE>> users/forms.py**
- create custom user creation and update forms classes

**users/admin.py**
- create custom user admin 
- register custom user and custom user admin

> $ python manage.py makemigrations
> $ python manage.py migrate

> $ python manage.py createsuperuser

**config/settings.py**
```[os.path.join(BASE_DIR, 'templates')],```
```LOGIN_REDIRECT_URL = 'home'```
```LOGOUT_REDIRECT_URL = 'home'```

**CREATE /templates**
- templates/registration/
- templates/registration/login.html
- templates/base.html
- templates/home.html
- templates/signup.html

**config/urls.py**

**CREATE users/urls.py**

**users.views.py**
