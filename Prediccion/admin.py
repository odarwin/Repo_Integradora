from django.contrib import admin

from Prediccion.models import Prediccion

@admin.register(Prediccion)
class PrediccionAdmin(admin.ModelAdmin):
    list_display=('title','description')
