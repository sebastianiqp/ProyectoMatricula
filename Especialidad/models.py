from django.db import models

# Create your models here.

class Especialidad(models.Model):
    cod_especialidad = models.CharField(max_length=10, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre