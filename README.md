initilize repo

**do not migrate until user model is authenticated with admin**

**config/settings.py**
INSTALLED_APPS = ```'users.spps.UsersConfig',```
AUTH_USER_MODEL = ```users.CustomUser```

**users/medels.py**
``` from django.contrib.auth.models import AbstractUser```
create custom user class inheriting AbstractUser