from django.contrib import admin
from .models import Course, District, TeeTime

# Register your models here.
admin.site.register(Course)
admin.site.register(District)
admin.site.register(TeeTime)
