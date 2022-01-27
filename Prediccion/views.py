from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from Imagen.models import Imagen
from Prediccion.models import Prediccion
from Prediccion.forms import PrediccionForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def guardarComentario(request):
    print("guardarComentario")
    id_=request.POST.get('id','')
    motivo=request.POST.get('motivoA','')
    estado=request.POST.get('state','')
    print(motivo)
    Prediccion.objects.filter(image=id_).update(description=motivo)
    Prediccion.objects.filter(image=id_).update(state=estado)
    return redirect('Imagen:cargarImagen') 

@csrf_exempt
def guardarPrediccion(request):
    print("guardarPrediccion")
    print(request)
    if request.method == 'GET':
        resultado={
            # 'image':request.id,
            'image':request.GET.get('id'),
            'title':request.GET.get('title',''),
            'resultado':'',
            'state':'A'
        }
        print(resultado)
        form = PrediccionForm(resultado)
        # print(form)
        if form.is_valid():
            form.save()
            # return redirect('Imagen:cargarImagen')
            if request.GET.get('name')=="aceptar":
                return render(request,'comentario/comentario_Aceptar.html',resultado)
            elif request.GET.get('name')=="rechazar":
                return render(request,'comentario/comentario_Rechazar.html',resultado)

        else:
            form=PrediccionForm()
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)