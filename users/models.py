# Django
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    CI=models.CharField(max_length=10,unique=True) #cedula
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        """Return username."""
        return self.user.username
