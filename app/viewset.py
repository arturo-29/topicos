from rest_framework import viewsets
from .serializer import *
from .models import *

class MatriculaViewset(viewsets.ModelViewSet):
    queryset = matricula.objects.all()
    serializer_class = MatriculaSerializer

class AlumnoViewset(viewsets.ModelViewSet):
    queryset = alumno.objects.all()
    serializer_class = AlumnoSerializer

class MateriaViewset(viewsets.ModelViewSet):
    queryset = materia.objects.all()
    serializer_class = MateriaSerializer

class DocenteViewset(viewsets.ModelViewSet):
    queryset = docente.objects.all()
    serializer_class = DocenteSerializer

class CalificacionViewset(viewsets.ModelViewSet):
    queryset = calificacion.objects.all()
    serializer_class = CalificacionSerializer