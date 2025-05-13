from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from accounts.models import CustomUser


@receiver(post_save, sender=CustomUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        print(f' Welcome saytimizga {instance.username}')


@receiver(pre_save, sender=CustomUser)
def last_name_default(sender, instance, **kwargs):
    if not instance.last_name:
        print(instance)
        instance.last_name = "UNKNOWN"


@receiver(post_delete, sender=CustomUser)
def user_info(sender, instance, **kwargs):
    print(f' Bye bye saytimizdan {instance.username}')