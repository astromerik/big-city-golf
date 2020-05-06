from django.db import models

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_firendly_name(self):
        return self.friendly_name

class Course(models.Model):
    district = models.ForeignKey('District', null=True, blank=True, on_delete=models.SET_NULL)
    course_name = models.CharField(max_length=50)
    holes = models.IntegerField(null=True, blank=True)
    green_fee = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    facility_url = models.URLField(max_length=1024, null=True, blank=True)
    img_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.course_name
