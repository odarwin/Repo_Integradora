from django.shortcuts import render, redirect,render_to_response
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from Imagen.models import Imagen
from Imagen.forms import CreateImagenForm

def cambiarPantalla(request ):
    return render(request, 'cargarImagen/cargarImagen.html', {})


class cargarImagenView(FormView):
    template_name = 'cargarImagen/cargarImagen.html'
    model = Imagen
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'Imagen'
    queryset = Imagen.objects.filter(status="A")
    form_class = CreateImagenForm
    


    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

@login_required
def guardar_ruta (request):
    if request.method=='POST':
        #aqui integrar el metodo de diagnostico y hacer que llene la descripcion
        imagen={
            'user': request.user.id,
            'profile': request.user.id,
            'title':request.POST.get('titulo',''),
            'pathImage':request.POST.get('rutaImagen',''),
            'status':'A',
            'description':ProcesarPrediccion()
            #Jocellyn en esta funcion iria el proceso de prediccion
        }
        form = CreateImagenForm(imagen)
        if form.is_valid():
            form.save()
            return redirect('Prediccion:Resultado')
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)

def ProcesarPrediccion():
    Resultado='Prediccion Prueba'
    return Resultado