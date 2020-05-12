from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    golf_id = models.CharField(max_length=10, null=True, blank=True)
    handicap = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
