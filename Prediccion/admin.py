from django.contrib import admin
from Imagen.models import Imagen

from Prediccion.models import Prediccion
from django.contrib.auth.models import User

@admin.register(Prediccion)
class PrediccionAdmin(admin.ModelAdmin):
    list_display=('id','image','title','description','state',)

