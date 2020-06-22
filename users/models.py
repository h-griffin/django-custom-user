from django.db import models
from django.config.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    