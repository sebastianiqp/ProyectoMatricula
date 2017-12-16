from django.db import models

# Create your models here.
from Especialidad.models import Especialidad
from Alumno.models import Alumno
from Docente.models import Docente
from Curso.models import Curso
from Categoria.models import Categoria

class Matricula(models.Model):
    cod_matricula = models.CharField(max_length=10, unique=True, blank=False, null=False)

    especialidad = models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)

    mfecha_matricula = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.cod_matricula