from ast import Pass
from tabnanny import verbose
from urllib import request
from django.db import models 
from time import timezone
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField("Nombre de la Categoria", max_length= 100, null = False, blank = False)
    estado = models.BooleanField("Categoria Activada/Categoria no Activada", default = True)
    fecha_creacion = models.DateField("Fecha de Creacion", auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField("Nombres de Autor", max_length = 255, null = False, blank=False)
    apellidos = models.CharField("Apellidos de Autor", max_length= 255, null= False,blank = False)
    facebook = models.URLField("Facebook", null = True, blank  = True)
    instagram = models.URLField("Instagram", null = True, blank  = True)
    web = models.URLField("Web", null = True, blank  = True)
    correo = models.URLField("Correo", null = True, blank  = True)
    estado = models.BooleanField("Autor Activo/No Activo", default= True)
    fecha_creacion = models.DateField("Fecha de Creacion", auto_now=False, auto_now_add= True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

class Post(models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField('Titulo', max_length=90,blank = False, null= False)
    slug = models.CharField('Slug', max_length=100, blank= False, null = False)
    descripcion = models.CharField('Descripción', max_length= 110, blank = False, null= False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=280, blank=False,null=False)
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default= True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) :
        return self.titulo

class Comentario(models.Model):
    nombre = models.CharField(max_length=60)
    comentario = models.TextField(max_length=400)

    def __str__(self) :
        return self.nombre



