from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from Imagen.models import Imagen
from Prediccion.models import Prediccion
from Prediccion.forms import PrediccionForm
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def verResultadoAprobar(request):
    print("verResultadoAprobar")
    print(request.GET.get('name'))
    if(request.GET.get('name')=="aceptaR"):
        return render(request,'comentario/comentario_Aceptar.html')
    elif (request.GET.get('name')=="rechazaR"):
        return render(request,'comentario/comentario_Rechazar.html')
    return HttpResponse("mala hp")
    
@csrf_exempt
def guardarPrediccion(request):
    print("guardarPrediccion")
    # print(request)
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
            # return redirect('Imagen:cargarImagen')
            return redirect('Prediccion:verResultadoAprobar')
        else:
            form=PrediccionForm()
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)