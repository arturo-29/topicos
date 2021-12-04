from rest_framework import serializers
from .models import *

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = matricula
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = '__all__'