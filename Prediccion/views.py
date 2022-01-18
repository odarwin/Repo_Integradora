from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from Imagen.models import Imagen
from Prediccion.models import Prediccion
from Prediccion.forms import PrediccionForm

@login_required
def guardarPrediccion(request):
    print("guardarPrediccion")
    imagen=Imagen.objects.order_by('-pk')[:1]
    print(imagen.pk)
    # enviarIdImagen('Prediccion:enviarId', id=)
    # if request.method == 'POST':
    if request.GET.get('name'):
        resultado={
            'image':imagen.pk,
            'title':imagen.title,
            'description':imagen.description
        }
        form = PrediccionForm(resultado)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)