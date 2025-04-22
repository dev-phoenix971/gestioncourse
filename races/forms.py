from django import forms
from .models import Race, RaceResult, Horse

class RaceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'date', 'location', 'distance', 'terrain', 'weather']


class HorseForm(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ['name', 'age', 'breed', 'trainer', 'owner', 'wins', 'losses']


class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResult
        fields = ['race', 'horse', 'jockey', 'position', 'time']


class RaceUpdateForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'date', 'location', 'distance', 'terrain', 'weather']


class HorseUpdateForm(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ['name', 'age', 'breed', 'trainer', 'owner', 'wins', 'losses']
