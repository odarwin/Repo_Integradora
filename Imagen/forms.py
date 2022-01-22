"""User forms."""

# Django
from django import forms

# Models
from Imagen.models import Imagen
from django.contrib.auth.models import User

class CreateImagenForm(forms.ModelForm):
    title=forms.CharField(max_length=100,widget=forms.TextInput())
    pathImage=forms.CharField(max_length=400,widget=forms.TextInput(),required=False)
    status=forms.CharField(max_length=1)
    description=forms.CharField(max_length=4000,widget=forms.TextInput())
    class Meta:
        model=Imagen
        fields=('user', 'profile','title','pathImage','status','description')

