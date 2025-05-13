from django.db import models
from accounts.models import CustomUser

class Transaction(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,related_name='from_user')
    to_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,related_name='to_user')
    amount = models.FloatField()




