from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from Imagen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='',
        view=TemplateView.as_view(template_name='home/home.html'),
        name='home'
    ),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('Imagen.urls', 'Imagen'), namespace='Imagen')),
    path('', include(('Prediccion.urls', 'Prediccion'), namespace='Prediccion')),
    path('', include(('aplicacionAdmin.urls', 'aplicacionAdmin'), namespace='aplicacionAdmin')),


]