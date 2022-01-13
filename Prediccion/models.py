from django.db import models

from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from Imagen.models import Imagen

class Prediccion (models.Model):
    image=models.ForeignKey(Imagen,on_delete=models.PROTECT)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=4000)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.description)

"""
IdPrediccion(PK)
Descripcion
idImagen(FK)"""