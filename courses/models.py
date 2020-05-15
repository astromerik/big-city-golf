from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from golfprofile.models import UserProfile
# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_firendly_name(self):
        return self.friendly_name


class Course(models.Model):
    district = models.ForeignKey(District, null=True, blank=True, on_delete=models.SET_NULL)
    course_name = models.CharField(max_length=50)
    course_description = models.TextField(null=True, blank=True)
    holes = models.IntegerField(null=True, blank=True)
    green_fee = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    facility_url = models.URLField(max_length=1024, null=True, blank=True)
    img_url = models.URLField(max_length=1024, null=True, blank=True)
    facility_phone = PhoneNumberField(null=True, blank=True)
    facility_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.course_name


class TeeTime(models.Model):
    tee_time = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    player = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tee_time)
