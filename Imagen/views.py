from django.shortcuts import render, redirect,render_to_response
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from Imagen.models import Imagen
from Imagen.forms import CreateImagenForm

class cargarImagen(FormView):
    template_name = 'cargarImagen/cargarImagen.html'
    # form_class = CreateImagenForm
    # success_url = reverse_lazy('')
    # return render_to_response('cargarImagen.html')

@login_required
def save_imagen (request):
    if request.method=='POST':
        imagen={
            'user': request.user.id,
            'profile': request.user.id,
            'title': 'Titulo Imagen',
            'pathImage':request.POST['imagen1'],
            'status':'A'
        }
        form = CreateImagenForm(imagen)
        if form.is_valid():
            form.save()
            return redirect('Imagen:cargarImagen')
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)