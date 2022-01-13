from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='',
        view=TemplateView.as_view(template_name='home/home.html'),
        name='home'
    ),
    path(
        route='cargarImagen',
        view=TemplateView.as_view(template_name='cargarImagen/cargarImagen.html'),
        name='cargarImagen'
    ),
    path(
        route='login',
        view=TemplateView.as_view(template_name='login/login.html'),
        name='login'
    ),
    path(
        route='resultado',
        view=TemplateView.as_view(template_name='resultado/resultado.html'),
        name='resultado'
    ),
    path(
        route='comentario',
        view=TemplateView.as_view(template_name='comentario/comentario.html'),
        name='comentario'
    ),


]
