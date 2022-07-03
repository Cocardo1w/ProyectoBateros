from ast import pattern
from django.urls import path
from appbateros.views import*
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('Inicio/', Inicio, name="inicio"),
    path('login', login_request, name='Login'),
    path('register/', register_request, name='Register'),
    path('contacto/', contacto, name="Contacto"),
    path('clases/', Clases, name="Clases"),
    path('Post/', post, name="Post"),
    path('base/', base, name="Base"),
    path('partituras/', partituras, name="Partituras"),
    path("actualizar_usuario/", actualizar_usuario, name="EditarUsuario"),
    path('logout/', LogoutView.as_view(template_name="appbateros/logout.html"), name="logout"),
    path('about/', about, name="About"),
    path('Bancodemusicos/', BancoMusicos, name="BancoMusicos")
]
