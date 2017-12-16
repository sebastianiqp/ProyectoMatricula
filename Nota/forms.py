from django import forms

from Nota.models import Nota


class NotaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_nota'].widget.attrs.update(
            {'placeholder': 'Codigo Nota', 'class': 'form-control'})

        self.fields['alumno'].widget.attrs.update(
            {'placeholder': 'Alumno', 'class': 'form-control'})

        self.fields['docente'].widget.attrs.update(
            {'placeholder': 'docente','class':'form-control'})

        self.fields['curso'].widget.attrs.update(
            {'placeholder': 'Curso', 'class': 'form-control'})

        self.fields['nota1'].widget.attrs.update(
            {'placeholder': 'Nota 1', 'class': 'form-control'})
        self.fields['nota2'].widget.attrs.update(
            {'placeholder': 'Nota 2', 'class': 'form-control'})
        self.fields['nota3'].widget.attrs.update(
            {'placeholder': 'Nota 3', 'class': 'form-control'})

        self.fields['promedio'].widget.attrs.update(
            {'placeholder': '´Promedio', 'class': 'form-control'})
        self.fields['estado'].widget.attrs.update(
            {'placeholder': '´Estado', 'class': 'form-control'})

    class Meta:
        model = Nota

        fields = [
            'cod_nota',
            'alumno',
            'docente',
            'curso',
            'nota1',
            'nota2',
            'nota3',
            'promedio',
            'estado',
        ]
        labels = {
            'cod_nota': 'Codigo Nota',
            'alumno': 'alumno',
            'docente': 'docente',
            'curso': 'curso',
            'nota1': 'Nota 1',
            'nota2': 'Nota 2',
            'nota3': 'Nota 3',
            'promedio': 'Promedio',
            'estado': 'Estado',
        }
