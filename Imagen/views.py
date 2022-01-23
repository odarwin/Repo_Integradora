from turtle import update
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.files.storage import default_storage
from Imagen.forms import CreateImagenForm
from django.views.decorators.csrf import csrf_exempt
from Imagen.models import Imagen
from django.conf import settings

@csrf_exempt
def cargarImagen(request):
    print("llegando")
    if request.method=='POST':
        path = ''
        print(request.FILES)
        for filename, file in request.FILES.items():
            path = 'nii\\' + request.FILES[filename].name
            print("saved as ", path)
            default_storage.save( path, file) #og
        imagen={
            'user': request.user.id,
            'profile': request.user.id,
            'title':request.POST.get('titulo',''),
            'pathImage': path,
            'status':'A',
            'description': ProcesarPrediccion(path), #og
            # 'description':'Descripcion Prueba',
        }
        print(imagen)
        form = CreateImagenForm(imagen)
        if form.is_valid() :
            form.save()
            imagen=Imagen.objects.order_by('-pk')[:1] 
            print(imagen)
            return render(request, 'resultado/resultado.html',{'imagen':imagen})
        else:
            print("Error al guardar la Imagen")
            return render(request,'cargarImagen/cargarImagen.html')  
    return render(request,'cargarImagen/cargarImagen.html')  
#og
#----------------------------------------ESEMBLE MODEL------------------------------------
import numpy as np
import SimpleITK as sitk
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
np.random.seed(777)
import math
import h5py
import tensorflow as tf
import keras
import keras.backend as K
from keras.models import Model
from tensorflow.keras.applications import DenseNet201
from tensorflow.keras.applications import VGG19
from keras.applications.inception_v3 import InceptionV3
from keras.applications.nasnet import NASNetMobile
from keras.layers import Input, concatenate, Dense
from keras.layers import GlobalAveragePooling2D

img_height, img_width = 224, 224
input_shape = (img_height, img_width, 3)
epochs = 1000
num_classes = 1
model_path = "esemble_model.h5"

def load_model():
    input_tensor = Input(shape = input_shape)  

    base_model1=NASNetMobile(input_shape= input_shape,weights='imagenet', include_top=False, input_tensor=input_tensor)
    base_model2=InceptionV3(input_shape= input_shape,weights='imagenet', include_top=False, input_tensor=input_tensor)
    base_model3=DenseNet201(input_shape= input_shape,weights='imagenet', include_top=False, input_tensor=input_tensor)
    base_model4=VGG19(input_shape= input_shape,weights='imagenet', include_top=False, input_tensor=input_tensor)

    x1 = base_model1.output
    x1 = GlobalAveragePooling2D()(x1)

    x2 = base_model2.output
    x2 = GlobalAveragePooling2D()(x2)

    x3 = base_model3.output
    x3 = GlobalAveragePooling2D()(x3)

    x4 = base_model4.output
    x4 = GlobalAveragePooling2D()(x4)

    merge = concatenate([x1, x2, x3 , x4])
    predictions = Dense(1, activation='sigmoid')(merge)

    return Model(inputs=input_tensor,outputs=predictions)

def get_slices_axial_3c(path):
    img = sitk.ReadImage(path, sitk.sitkFloat64)
    arr = sitk.GetArrayFromImage(img)
    arr = arr[49:68,:,:]

    slices = None
    count = 0

    for i in range(arr.shape[0]):
        slice = arr[arr.shape[0] - i -1, : , : ]
        slice = cv2.resize(slice, (img_height, img_width), interpolation=cv2.INTER_CUBIC)
        slice[slice < 0] = 0
        if slice.max() != 0:
            slice = cv2.merge((slice,slice,slice))
            if count == 0:
                slices = np.array([slice])
            else:
                slices = np.concatenate((slices,[slice]))
        count+=1
    return slices


model = load_model()
model.load_weights(model_path)

def evaluate_nii(path):
    slices = get_slices_axial_3c(path)
    preds = model.predict(slices)
    return preds.mean()

#-----------------------------------GRADCAM IMAGE-----------------------------------------------

#-----------------------------------PREDICTION-----------------------------------------------
def ProcesarPrediccion(path):
    pred = evaluate_nii(settings.MEDIA_ROOT + '\\' + path)
    message = "La imagen es de un paciente que padece {desease:s}.\nEl porcentaje de predicción fue de {pred:.3f}."
    if pred > 0.5:
        message = message.format(desease="sólo la enfermedad de Parkinson", pred=(pred))
    else:
        message = message.format(desease="la enfermedad de Parkinson y algún ICD", pred=(1 - pred))
    return message
