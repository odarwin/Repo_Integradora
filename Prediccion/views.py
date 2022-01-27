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
    if(request.GET.get('name')=="aceptar"):
        return render(request,'comentario/comentario_Aceptar.html', {'title':request.GET.get('title') , 'id':request.GET.get('id')})
    elif (request.GET.get('name')=="rechazar"):
        return render(request,'comentario/comentario_Rechazar.html', {'title':request.GET.get('title') , 'id':request.GET.get('id') })
    return HttpResponse("mala hp")
    
def guardarPrediccion(request):
    print("guardarPrediccion")
    if request.method == 'POST':
    # if request.GET.get('name'):
        message = "none"
        print(request.POST)
        if request.POST.get('resultados','') != '':
            message = request.POST.get('resultados','')
        resultado={
            'image':request.POST.get('id')[:-1],
            'title':request.POST.get('title')[:-1],
            'resultado': message ,
            'state':request.POST.get('state')
        }
        form = PrediccionForm(resultado)
        if form.is_valid():
            form.save()
            print("saved")
        else:
            form=PrediccionForm()
        return redirect('Imagen:cargarImagen')