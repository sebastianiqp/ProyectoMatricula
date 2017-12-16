from django import forms

from Alumno.models import Alumno


class AlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_alumno'].widget.attrs.update(
            {'placeholder': 'Codigo Alumno', 'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(
            {'placeholder': 'Nombre', 'class':'form-control'})
        self.fields['apellido'].widget.attrs.update(
            {'placeholder': 'Apellido', 'class': 'form-control'})
        self.fields['dni'].widget.attrs.update(
            {'placeholder': 'Dni', 'class': 'form-control'})
        self.fields['sexo'].widget.attrs.update(
            {'placeholder': 'Sexo', 'class': 'form-control'})
        self.fields['edad'].widget.attrs.update(
            {'placeholder': 'Edad', 'class': 'form-control'})
        self.fields['fecha_nacimiento'].widget.attrs.update(
            {'placeholder': 'Fecha Nacimiento', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Correo', 'class': 'form-control'})
        self.fields['afecha_registro'].widget.attrs.update(
            {'placeholder': 'Fecha Registro', 'class': 'form-control'})

    class Meta:
        model = Alumno

        fields = [
            'cod_alumno',
            'nombre',
            'apellido',
            'dni',
            'sexo',
            'edad',
            'fecha_nacimiento',
            'email',
            'afecha_registro',
        ]
        labels = {
            'cod_alumno': 'Codigo Alumno',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni': 'Dni',
            'sexo': 'Sexo',
            'edad': 'Edad',
            'fecha_nacimiento': 'Fecha Nacimiento',
            'email': 'Email',
            'afecha_registro': 'Fecha de Registro',
        }

