from django import forms
from django.forms import ModelForm
from .models import Attendant

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class PromiseForm(ModelForm):
    class Meta:
        model = Attendant
        fields = ['MemberID', 'Start', 'End', 'Info']
        widgets = {
            'Start': DateInput(),
            'End': DateInput(),
        }