from django.urls import path
from aplicacionAdmin import views
urlpatterns = [

    path(
        route='aplicacionAdmin/usuarios',
        view=views.cargarUsuarios,
        name='cargarUsuarios'
    ),
    path(
        route='aplicacionAdmin/recursos',
        view=views.cargarRecursos,
        name='cargarRecursos'
    ),
    
]