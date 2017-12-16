from django import forms

from Curso.models import Curso

class CursoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_curso'].widget.attrs.update(
            {'placeholder': 'Codigo Curso', 'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(
            {'placeholder': 'nombre','class':'form-control'})
        self.fields['creditos'].widget.attrs.update(
            {'placeholder': 'creditos', 'class': 'form-control'})


    class Meta:
        model = Curso

        fields = [
            'cod_curso',
            'nombre',
            'creditos',
        ]
        labels = {
            'cod_curso': 'Codigo Curso',
            'nombre': 'Nombre',
            'creditos': 'Creditos',
        }
