from ast import pattern
from django.urls import path
from appbateros.views import*

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login', login_request, name='Login'),
    path('register', register_request, name='Register'),
    path('contacto/', contacto, name="Contacto"),
    # path('Post/', post, name="Post"),
    path('base/', base, name="Base"),
    path('partituras/', partituras, name="Partituras"),
    path('about/', about, name="About"),
]
