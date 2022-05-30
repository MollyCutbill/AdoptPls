from unicodedata import name
from django.urls import path

from .views import index
from .views import formUsuario
from .views import adminUsuarios
from .views import formModUsuario
from .views import formElimUsuario
from .views import api
from .views import comida
from .views import cosas_gatos
from .views import cosas_perros
from .views import formulario_de_contacto
from .views import gato
from .views import iniciar_sesion
from .views import perro
from .views import usuario
from .views import veterinario

urlpatterns = [
    path('', index, name="index"),
    path('formUsuario', formUsuario, name="formUsuario"),
    path('adminUsuarios', adminUsuarios, name="adminUsuarios"),
    path('formModUsuario/<id>', formModUsuario, name="formModUsuario"),
    path('formElimUsuario/<id>', formElimUsuario, name="formElimUsuario"),
    path('comida', comida, name="comida"),
    path('cosas_gatos',cosas_gatos , name="cosas_gatos"),
    path('cosas_perros',cosas_perros , name="cosas_perros"),
    path('formulario_de_contacto',formulario_de_contacto, name="formulario_de_contacto"),
    path('gato',gato , name="gato"),
    path('iniciar_sesion',iniciar_sesion , name="iniciar_sesion"),
    path('perro',perro , name="perro"),
    path('usuario',usuario , name="usuario"),
    path('veterinario',veterinario , name="veterinario")
    
    
    
#

    
]