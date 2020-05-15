import uuid
from django.db import models
from golfprofile.models import UserProfile
from courses.models import TeeTime, Course
from django.db.models import Sum
# Create your models here.

class TeeTimePurchase(models.Model):
    order_number = models.CharField(max_length=40, null=True, blank=True)
    tee_time = models.ForeignKey(TeeTime, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField('Created time', auto_now_add=True)
    total_greenfee = models.IntegerField(blank=False, null=False)


    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_greenfee(self):
        self.total_greenfee = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()
    
    def __str__(self):
        return str(self.player)

