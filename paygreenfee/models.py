from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from golfprofile.models import UserProfile
from courses.models import TeeTime, Course
from django.db.models import Sum
# Create your models here.

class TeeTimePurchase(models.Model):
    tee_time = models.ForeignKey(TeeTime, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    total_greenfee = models.IntegerField(blank=False, null=False)

    def update_greenfee(self):
        self.total_greenfee = lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        self.lineitem_total = self.course.greenfee
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.tee_time