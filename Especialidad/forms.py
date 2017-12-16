from django import forms

from Especialidad.models import Especialidad

class EspecialiadadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_especialidad'].widget.attrs.update(
            {'placeholder': 'Codigo Especialidad', 'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(
            {'placeholder': 'Nombre Especialidad','class':'form-control'})

    class Meta:
        model = Especialidad

        fields = [
            'cod_especialidad',
            'nombre',
        ]
        labels = {
             'cod_especialidad': 'Codigo Especialidad',
             'nombre': 'Nombre'
        }

