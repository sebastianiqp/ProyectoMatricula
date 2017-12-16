from django.db import models

# Create your models here.

class Categoria(models.Model):
    cod_categoria = models.CharField(max_length=10, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre