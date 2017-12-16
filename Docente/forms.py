from django import forms

from Docente.models import Docente

class DocenteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_docente'].widget.attrs.update(
            {'placeholder': 'Codigo del Docente', 'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(
            {'placeholder': 'Nombre del Docente','class':'form-control'})
        self.fields['apellido'].widget.attrs.update(
            {'placeholder': 'Apellido del Docente', 'class': 'form-control'})
        self.fields['dni'].widget.attrs.update(
            {'placeholder': 'DNI', 'class': 'form-control'})
        self.fields['sexo'].widget.attrs.update(
            {'placeholder': 'Sexo', 'class': 'form-control'})
        self.fields['especialidad'].widget.attrs.update(
            {'placeholder': 'Especialidad', 'class': 'form-control'})
        self.fields['direccion'].widget.attrs.update(
            {'placeholder': 'Direccion', 'class': 'form-control'})
        self.fields['curso'].widget.attrs.update(
            {'placeholder': 'curso', 'class': 'form-control'})

    class Meta:
        model = Docente

        fields = [
            'cod_docente',
            'nombre',
            'apellido',
            'dni',
            'sexo',
            'especialidad',
            'direccion',
            'curso',
        ]
        labels = {
             'cod_docente': 'Codigo Alumno',
             'nombre': 'Nombre',
             'apellido': 'Apellido',
             'dni': 'Dni',
             'sexo': 'Sexo',
             'especialidad': 'Especialidad',
             'direccion': 'Direccion',
             'curso': 'curso',
        }

