from django import forms
from .models import TeeTime


class TeeTimeForm(forms.ModelForm):
    class Meta:
        model = TeeTime
        fields = ['tee_time', 'course', 'price']
