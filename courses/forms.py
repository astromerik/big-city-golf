from django import forms
from .models import TeeTime


class TeeTimeForm(forms.ModelForm):
    class Meta:
        model = TeeTime
        fields = ['day_to_play', 'tee_time', 'course', 'player',]
