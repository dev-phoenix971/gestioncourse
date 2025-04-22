from django import forms
from .models import Bet
from races.models import Race

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['race', 'selected_horses', 'bet_type', 'amount']

    def __init__(self, *args, **kwargs):
        super(BetForm, self).__init__(*args, **kwargs)
        self.fields['race'].queryset = Race.objects.filter(date__year=2025, location="Vincennes")
