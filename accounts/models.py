from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class RoleChoice(models.TextChoices):
    ADMIN=('admin','Admin')
    PUBLISHER=('publisher','Publisher')
    READER=('reader','Reader')

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11,blank=True,null=True)
    role=models.CharField(max_length=50,choices=RoleChoice,default=RoleChoice.READER)
    balance=models.PositiveIntegerField(default=3000)


def code_generate():
    return str(random.randint(100000,999999))

def get_expire_time():
    return timezone.now() + timedelta(minutes=2)


class Code(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    code=models.CharField(default=code_generate,max_length=6)
    expire_date=models.DateTimeField(default=get_expire_time)






