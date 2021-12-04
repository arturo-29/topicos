from django.db import models

class persona(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    apellido = models.CharField(max_length=45, blank=False)
    telefono = models.IntegerField(blank=False)
    correo = models.EmailField(blank=False)
    direccion = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.nombre

tipo_matricula = [
    ('ORDINARIA', 'ORDINARIA'),
    ('REPITE', 'REPITE'),
    ('ESPECIAL', 'ESPECIAL'),
]

class matricula(models.Model):
    codigo = models.CharField(max_length=8, blank=False)
    tipo = models.CharField(max_length=45, choices=tipo_matricula, default='available')
    carrera = models.CharField(max_length=25, blank=False)
    fk_persona = models.OneToOneField(persona, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.codigo