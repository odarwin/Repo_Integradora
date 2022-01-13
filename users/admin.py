# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile
# user y profile van de la mano

# Con admin.register(Profile) registramos nuestro modelo lo que hará que nos aparezca en el panel.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display: Nos mostrará la lista de usuarios creados cuando estemos en el apartado de profile, 
    # la información que se mostrará es la que añadamos en la lista, en este caso la primary key, el usuario y la foto.
    list_display = ('pk', 'user', 'CI')


    # list_display_links: Añadirá un link para la edición en 
    # los campos que especifiquemos, en este caso en la primary key y en el usuario.
    list_display_links = ('pk', 'user',)

    # list_editable: Esta funcionalidad nos permitirá editar la foto de un usuario desde el panel de listados.

    # list_editable = ('photo',)

# search_fields: Permite la busqueda por los campos que añadas.

    search_fields = (
        'user__firstname',
        'user__lastname',
    )

    # list_filter: Añade un panel de filtros con los campos que hemos añadido.
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'date_modified',
    )
# field_sets: Permite customizar como se visualizarán los datos en el panel,
#  en nuestro caso, profile y metadata serían las cabeceras de los campos y dentro 
# de fields si los datos están dentro de una tupla aparecerán horizontalmente (nuestro caso), sino verticalmente.

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'CI', 'firstName','lastName'),),
        }),
        ('Extra info', {
            'fields': (('date_modified'),),
        })
    )
    # readonly_fields: Los datos que añadas aquí se mostrarán solo como lectura.
    readonly_fields = (('date_modified'),)

    """Profile in-line admin for users."""
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
"""
Lo que hacemos aquí es crear la clase ProfileInline y en está guardamos 
el modelo que queremos añadir al modelo padre.
Después lo que tenemos que hacer es quitar la clase User que es la que está por defecto
 y registrar nuestra nueva clase, entonces declaramos nuestra nueva clase, añadimos la clase de tipo StackedInline y en el list_display metemos los datos que queremos que se muestren al listar los usuarios.
Por último utilizamos el metodo unregister para quitar nuestra clase User y registramos 
la nueva clase pasando el modelo base y la nueva clase. 
"""
admin.site.unregister(User)
admin.site.register(User, UserAdmin)




