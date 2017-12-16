from django.db import models

# Create your models here.
from Alumno.models import Alumno
from Docente.models import Docente
from Curso.models import Curso

class Nota(models.Model):
    cod_nota = models.CharField(max_length=10, unique=True, blank=False, null=False)

    alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)

    nota1 = models.IntegerField(default=0, blank=True, null=True)
    nota2 = models.IntegerField(default=0, blank=True, null=True)
    nota3 = models.IntegerField(default=0, blank=True, null=True)
    promedio = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    estado = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.cod_nota