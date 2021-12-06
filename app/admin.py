from django.contrib import admin
from .models import *


class alumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo', 'direccion')

class matriculaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fk_alumno', 'tipo', 'carrera')
    
class materiaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fk_docente', 'nombre', 'fk_docente')

class docenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo', 'direccion')

class calificacionAdmin(admin.ModelAdmin):
    list_display = ('porcentaje', 'fk_alumno', 'fk_materia', 'fk_docente')

admin.site.register(alumno, alumnoAdmin)
admin.site.register(matricula, matriculaAdmin)
admin.site.register(materia, materiaAdmin)
admin.site.register(docente, docenteAdmin)
admin.site.register(calificacion, calificacionAdmin)