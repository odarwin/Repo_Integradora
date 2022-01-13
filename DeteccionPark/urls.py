from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

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
        route='resultado',
        view=TemplateView.as_view(template_name='resultado/resultado.html'),
        name='resultado'
    ),
    path(
        route='comentario',
        view=TemplateView.as_view(template_name='comentario/comentario.html'),
        name='comentario'
    ),
    path('', include(('users.urls', 'users'), namespace='users')),
    # path('', include(('Imagen.urls', 'Imagen'), namespace='Imagen')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
