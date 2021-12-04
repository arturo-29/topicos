from django.contrib import admin
from .models import *


class personaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo', 'direccion')

class matriculaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fk_persona', 'tipo', 'carrera')

admin.site.register(persona, personaAdmin)
admin.site.register(matricula, matriculaAdmin)