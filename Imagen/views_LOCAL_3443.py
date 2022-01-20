from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Imagen.forms import CreateImagenForm
from django.views.decorators.csrf import csrf_exempt



from Imagen.models import Imagen
@csrf_exempt
def cargarPantallaImagen(request):
    return render(request,'cargarImagen/cargarImagen.html',{})

@csrf_exempt
def guardarImagen(request):
    print("llegando")
    ruta = "C:\\Users\\Darwin\\Documents\\PROYECTOS\\Integradora\\DeteccionPark\\Papaya\\images\\"
    if request.method=='POST':
        #aqui integrar el metodo de diagnostico y hacer que llene la descripcion
        imagen={
            'user': request.user.id,
            'profile': request.user.id,
            'title':request.POST.get('titulo',''),
            'pathImage':ruta + request.POST.get('rutaImagen',''),
            'status':'A',
            'description':ProcesarPrediccion(),
            #Jocellyn en esta funcion iria el proceso de prediccion
        }
        form = CreateImagenForm(imagen)
        if form.is_valid() :
            form.save()
            imagen=Imagen.objects.order_by('-pk')[:1] 
            print(imagen)
            return render(request, 'resultado/resultado.html',{'imagen':imagen})
            # return HttpResponse(status=200)

    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)
    
def ProcesarPrediccion():
    Resultado='Prediccion Prueba'
    return Resultado