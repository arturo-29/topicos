from rest_framework import serializers
from .models import *

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = matricula
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = alumno
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = materia
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = docente
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = calificacion
        fields = '__all__'