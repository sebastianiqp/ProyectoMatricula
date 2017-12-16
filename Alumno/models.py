from django.db import models


# Create your models here.
class Alumno(models.Model):
    cod_alumno = models.CharField(max_length=10, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    dni = models.CharField(max_length=10, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=50)
    afecha_registro = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(str(self.nombre), str(self.apellido))
