from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import TeeTimePurchase


@receiver(post_save, sender=TeeTimePurchase)
def update_greenfee(sender, instance, created, **kwargs):
    instance.greenfe.update_greenfee()


@receiver(post_delete, sender=TeeTimePurchase)
def delete_greenfee(sender, instance, **kwargs):
    instance.greenfe.update_greenfee()
