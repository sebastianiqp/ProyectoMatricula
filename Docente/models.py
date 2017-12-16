from django.db import models


from Curso.models import Curso

# Create your models here.
class Docente(models.Model):
    cod_docente = models.CharField(max_length=10, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    dni = models.IntegerField()
    sexo = models.CharField(max_length=10, blank=False, null=False)
    especialidad = models.CharField(max_length=10,blank=False, null=False)
    direccion = models.CharField(max_length=50,blank=False, null=False)

    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(str(self.nombre), str(self.apellido))

