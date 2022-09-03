from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email=models.EmailField(verbose_name='email',max_length=255,unique=True)
    phoneno=models.CharField(verbose_name='phone_no',max_length=255)

    REQUIRED_FIELDS= ['email','phoneno']

    def get_username(self) -> str:
        return self.email