from rest_framework.serializers import ModelSerializer
from Alumno.models import Alumno


class AlumnoSerializer(ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id', 'cod_alumno',)
        #fields =  '__all__'
