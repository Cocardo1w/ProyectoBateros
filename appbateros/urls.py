from ast import pattern
from django.urls import path
from appbateros.views import*

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('Post/', post, name="Post"),
    path('base/', base, name="Base"),
    path('partituras/', partituras, name="Partituras"),
    path('contacto/', contacto, name="Contacto"),
    path('login', login_request, name='Login'),
]
