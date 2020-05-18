import uuid
from django.db import models
from golfprofile.models import UserProfile
from courses.models import TeeTime, Course
from django.db.models import Sum
# Create your models here.

# For information and transaction
class PaymentInfo(models.Model):
    order_number = models.CharField(max_length=40, null=True, blank=False, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=True, blank=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
    total_greenfee = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_greenfee(self):
        self.total_greenfee = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

# After transaction is completed
class TeeTimePurchase(models.Model):

    # purchase_info = models.ForeignKey(PurchaseInfo, null=False, blank=False, on_delete=models.CASCADE)
    tee_time = models.ForeignKey(TeeTime, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    total_greenfee = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.total_greenfee = self.course.greenfee * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.player)
