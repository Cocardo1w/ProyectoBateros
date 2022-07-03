from tkinter import Label
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ComentarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=60)
    comentario = forms.CharField(widget=forms.Textarea)

class UsuarioEditForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia 2', widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password1', 'password2']
        help_text = { k: "" for k in fields}

