from django.urls import path

# Views
from Prediccion import views

urlpatterns = [
    path(
        route='Resultado',
        view=views.MostrarImagen,
        name='Resultado'
    ),
    path(
        route='ResultadoImagen',
        view=views.MostrarResultado,
        name='ResultadoImagen'
    ),
    path(
        route='Comentario',
        view=views.MostrarComentario,
        name='Comentario'
    ),

]