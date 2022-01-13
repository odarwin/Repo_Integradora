"""User forms."""

# Django
from django import forms

# Models
from Imagen.models import Imagen
from django.contrib.auth.models import User

class CreateImagenForm(forms.ModelForm):
    ruta_imagen=forms.CharField(max_length=400)

class Meta:
    # user = User.objects.create_user(data['username'],data['email'],data['password'])
    model=Imagen
    fields=('user','profile','title','pathImage','status')

