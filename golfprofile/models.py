from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone_number = PhoneNumberField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    golf_id = models.CharField(max_length=10, null=True, blank=True)
    handicap = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.user.username

