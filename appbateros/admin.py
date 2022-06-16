from django.contrib import admin
from appbateros.models import Autor, Categoria

from appbateros.views import post
from appbateros.models import *


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre'] #barra de busqueda
    list_display = ('nombre','estado','fecha_creacion',)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos','correo']
    list_display = ('nombres', 'apellidos','correo','estado','fecha_creacion')


# Register your models here.

admin.site.register(Categoria, CategoriaAdmin) #Categoria es una instancia del modelo
admin.site.register(Autor, AutorAdmin)

