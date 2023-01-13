from django import forms
from django.forms import ModelForm
from .models import LeaveApply

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class PromiseForm(ModelForm):
    class Meta:
        model = LeaveApply
        fields = ['Start', 'End', 'Info']
        widgets = {
            'Start': DateInput(),
            'End': DateInput(),
        }
