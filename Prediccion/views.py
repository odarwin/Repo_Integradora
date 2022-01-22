from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from Imagen.models import Imagen
from Prediccion.models import Prediccion
from Prediccion.forms import PrediccionForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def guardarPrediccion(request):
    print("guardarPrediccion")
    print(request)
    if request.method == 'POST':
    # if request.GET.get('name'):
        resultado={
            # 'image':request.id,
            'image':request.POST.get('id'),
            'title':request.POST.get('Imagen de Paciente',''),
            'resultado':request.POST.get('resultados',''),
            'state':'A'
        }
        print(resultado)
        form = PrediccionForm(resultado)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=PrediccionForm()
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)