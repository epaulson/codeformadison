from django import forms
from core.models import BusStop, Profile

class BusStopForm(forms.ModelForm):
    class Meta:
        model = BusStop
        exclude = ('owner',)
