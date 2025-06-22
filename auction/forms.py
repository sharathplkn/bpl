from django import forms
from .models import team  # Ensure the correct model is imported

class AuctionForm(forms.Form):
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        initial=20,
        label="Set Price"
    )
    team = forms.ModelChoiceField(
        queryset=team.objects.all(),  # Ensure you are using the correct model name 'Team'
        widget=forms.RadioSelect(attrs={'class': 'radio-inputs'}),
        label="Select Team"
    )