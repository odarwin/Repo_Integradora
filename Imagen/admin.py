from django.contrib import admin
from Imagen.models import Imagen

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'pathImage','description')
    search_fields=(('title'),)
    list_filter=('title','description')
    def get_form(self, request, obj=None, **kwargs):   
        form = super(ImagenAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['profile'].initial = request.user.profile

        return form
"""Para este caso hemos añadido el método get_form que lo que
 hace es que nos permite realizar cambios en el formulario
  antes de mostrarlo. 
"""