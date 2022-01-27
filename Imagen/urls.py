"""Posts URLs."""

# Django
from django.urls import path

# Views
from Imagen import views

urlpatterns = [
 path(
        route='cargarImagen',
        view=views.cargarImagen,
        name='cargarImagen'
    ),
    


]