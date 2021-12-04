from rest_framework import viewsets
from .serializer import *
from .models import *

class MatriculaViewset(viewsets.ModelViewSet):
    queryset = matricula.objects.all()
    serializer_class = MatriculaSerializer

class PersonaViewset(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer