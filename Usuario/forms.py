from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'first_name', 'class': 'form-control'})

        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'last_name', 'class': 'form-control'})

        self.fields['username'].widget.attrs.update(
            {'placeholder': 'username', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Correo', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'password1', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'password2', 'class': 'form-control'})

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
             'first_name': 'first name',
             'last_name': 'last name',
             'username': 'username',
             'email': 'email',
             'password1': 'password1',
             'password2': 'password2',
        }

