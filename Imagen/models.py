# Django
from django.db import models

from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Imagen(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)
    title=models.CharField(max_length=100)
    pathImage=models.CharField(max_length=400)
    date_upload = models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=4000)
    status=models.CharField(max_length=1)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username,
        self.pathImage,self.description,self.status)

    # def save(self, *args, **kwargs):
    #     self.title = slugify(self.title)
    #     super(Imagen, self).save(*args, **kwargs)

"""IdImagen(PK)
idMedico(FK)
Titulo
RutaImagen
FechaRegistro
Descripcion
Estado
IdAdministrador(FK)
"""
