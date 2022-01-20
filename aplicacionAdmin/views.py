from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Imagen.models import Imagen
from Prediccion.models import Prediccion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views 
from django.contrib.auth.models import User

def cargarUsuarios(request):
    usuarios=request.user.profile
    print(usuarios)
    # return render(request, 'Administrador/usuarios.html',{'usuarios':usuarios})


def cargarRecursos(request):
    imagenes=Imagen.objects.all()
    imagenes_={
        'imagenes':imagenes,
    }
    return render(request,'Administrador/recursos.html',imagenes_)