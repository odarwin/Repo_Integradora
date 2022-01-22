# Django
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    CI=models.CharField(max_length=10,unique=True) #cedula
    roles=[
        ('M','MEDICO'),
        ('A','ADMINISTRADOR')
    ]
    rol=models.CharField(max_length=1,choices=roles,default='M')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        """Return username."""
        # return self.user.username,self.rol
        return '{} {} {}'.format(self.firstName, self.lastName, self.rol)


    def nombreCompleto(self):
        txt="{0} {1} tiene un rol de {2}"
        return txt.format(self.firstName,self.lastName,self.rol)