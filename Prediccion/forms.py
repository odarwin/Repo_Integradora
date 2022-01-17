"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from Prediccion.models import Prediccion

class PrediccionForm(forms.ModelForm):
    title=forms.CharField(max_length=100)
    resultado=forms.CharField(max_length=4000,widget=forms.Textarea)

    class Meta:
        Model:Prediccion
        fields=('user', 'profile', 'title', 'resultado')