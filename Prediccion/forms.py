"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from Prediccion.models import Prediccion
from Imagen.models import Imagen

class PrediccionForm(forms.ModelForm):
    title=forms.CharField(max_length=100,widget=forms.TextInput())
    resultado=forms.CharField(max_length=4000,widget=forms.Textarea)
    state=forms.CharField(max_length=1)
    class Meta:
        model=Prediccion
        fields=('image','title', 'resultado','state',)   