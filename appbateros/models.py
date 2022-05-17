from urllib import request
from django.db import models 
from time import timezone
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    nombre = models.CharField(max_length=40)
    contenido = models.TextField(max_length=800)
    imagen = models.URLField()
    autor = models.CharField(max_length=40)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
