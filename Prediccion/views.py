from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from Imagen.models import Imagen
from Prediccion.models import Prediccion
from Prediccion.forms import PrediccionForm

# class CambiarPantalla (DetailView,slug):
#     template_name = 'resultado/resultado.html'
#     # render(request, 'cargarImagen/cargarImagen.html', {})
#     model = Prediccion
#     context_object_name = 'Prediccion'
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['description']=Imagen.objects.filter(title=slug)
#         return context

def MostrarComentario(request):
    return render(request, 'comentario/comentario.html', {})

def MostrarResultado(request):
    return render(request, 'resultado/resultado.html', {})

def MostrarImagen(request):  
    # imagen=Imagen.objects.filter(title__contains=pk)
    imagen=Imagen.objects.order_by('-pk')[:1]
    # form=PrediccionForm(imagen)
    if request.method == 'POST':
        form = PrediccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Prediccion:ResultadoImagen')
    
    else:

        context = {
        'Imagen':imagen,
        # 'form': form
        }
        # return redirect('Prediccion:Comentario')
        print(context)
        return render(request, 'resultado/resultado.html', context)

    return HttpResponse(status=500)
    # return render(request, 'comentario', context)
