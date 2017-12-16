from django.db import models

# Create your models here.
class Curso(models.Model):
    cod_curso = models.CharField(max_length=10, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre
