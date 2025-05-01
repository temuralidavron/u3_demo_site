from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleChoice(models.TextChoices):
    ADMIN=('admin','Admin')
    PUBLISHER=('publisher','Publisher')
    READER=('reader','Reader')

class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=11,blank=True,null=True)
    role=models.CharField(max_length=50,choices=RoleChoice,default=RoleChoice.READER)