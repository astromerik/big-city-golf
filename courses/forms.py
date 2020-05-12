from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class ExampleForm(forms.form):
    my_date_field = forms.DateField(widget=DateInput)