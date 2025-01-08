from django import forms
from .models import *
class AuctionForm(forms.Form):
    price = forms.DecimalField(max_digits=10, decimal_places=2, initial=20, label="Set Price", required=False)
    team = forms.ModelChoiceField(queryset=team.objects.all(), label="Select Team", required=False)  # Make team optional
