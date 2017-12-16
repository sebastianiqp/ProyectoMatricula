from django import forms

from Matricula.models import Matricula


class MatriculaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_matricula'].widget.attrs.update(
            {'placeholder': 'Codigo Matricula', 'class': 'form-control'})
        self.fields['especialidad'].widget.attrs.update(
            {'placeholder': 'Nombre Especialidad', 'class': 'form-control'})
        self.fields['alumno'].widget.attrs.update(
            {'placeholder': 'Nombre Alumno', 'class': 'form-control'})
        self.fields['docente'].widget.attrs.update(
            {'placeholder': 'Nombre del Docente', 'class': 'form-control'})
        self.fields['curso'].widget.attrs.update(
            {'placeholder': 'Nombre del Curso', 'class': 'form-control'})

        self.fields['categoria'].widget.attrs.update(
            {'placeholder': 'Categoria', 'class': 'form-control'})

        self.fields['mfecha_matricula'].widget.attrs.update(
            {'placeholder': 'Registro de Matricula', 'class': 'form-control'})

    class Meta:
        model = Matricula

        fields = [
            'cod_matricula',
            'especialidad',
            'alumno',
            'docente',
            'curso',
            'categoria',
            'mfecha_matricula',
        ]
        labels = {
            'cod_matricula': 'Codigo Matricula',
            'especialidad': 'Especialidad',
            'alumno': 'Alumno',
            'docente': 'Docente',
            'curso': 'Curso',
            'categoria': 'Categoria',
            'mfecha_matricula': 'Fecha de Registro',
        }
