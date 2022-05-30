from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Usuario

#clase para el formulario desde la bd
class UsuarioForm(ModelForm):
    
    class Meta:
        model = Usuario
        fields =['correo','nombre','telefono','password']