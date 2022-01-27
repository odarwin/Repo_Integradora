from django.urls import path

# Views
from Prediccion import views
from django.views.generic import TemplateView

urlpatterns = [
    
    path(
        route='guardarPrediccion',
        view=views.guardarPrediccion,
        name='guardarPrediccion'
    ),
    path(
        route='prediccion/verResultadoAprobar',
        view=views.verResultadoAprobar,
        name='verResultadoAprobar'
    ),
    

]