# forms.py
from django import forms
from .models import AMP, TargetProtein, Dock
class SearchForm(forms.Form):
    amp = forms.ModelChoiceField(queryset=AMP.objects.all())
    target_proteins = forms.ModelMultipleChoiceField(queryset=TargetProtein.objects.all())
