from django import forms

from Categoria.models import Categoria

class CategoriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_categoria'].widget.attrs.update(
            {'placeholder': 'Codigo Categoria', 'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(
            {'placeholder': 'Nombre Especialidad','class':'form-control'})

    class Meta:
        model = Categoria

        fields = [
            'cod_categoria',
            'nombre',
        ]
        labels = {
             'cod_categoria': 'Codigo Categoria',
             'nombre': 'Nombre'
        }

