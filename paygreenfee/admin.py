from django.contrib import admin
from .models import TeeTimePurchase

# Register your models here.

class TeeTimeAdmin(admin.ModelAdmin):
    model = TeeTimePurchase
    readonly_fields = ('player')

admin.site.register(TeeTimePurchase)
