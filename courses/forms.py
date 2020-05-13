from django import forms
from .models import TeeTime


class DateInput(forms.DateInput):
    input_type = 'date'


class ExampleForm(forms.form):
    my_date_field = forms.DateField(widget=DateInput)


class TeeTimeForm(forms.form):
    model = TeeTime
    fields = ['day_to_play', 'tee_time', 'course', 'player', 'booked']
