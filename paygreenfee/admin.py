from django.contrib import admin
from .models import TeeTimePurchase, PaymentInfo

# Register your models here.


class TeeTimePurchaseAdmin(admin.TabularInline):
    model = TeeTimePurchase
    readonly_fields = ('player')


class PaymentInfoAdmin(admin.ModelAdmin):
    inlines = (TeeTimePurchaseAdmin)

    readonly_fields = ('order_number', 'purchase_date', 'total_greenfee', 'stripe_pid')

    fields = ('order_number', 'first_name', 'last_name', 'email', 'phone_number', 'purchase_date', 'total_greenfee', 'stripe_pid')

    list_display = ('order_number', 'purchase_date', 'first_name', 'last_name', 'total_greenfee')


admin.site.register(TeeTimePurchase)
admin.site.register(PaymentInfo)
