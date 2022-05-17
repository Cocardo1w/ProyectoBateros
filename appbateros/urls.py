from ast import pattern
from django.urls import path
from appbateros.views import*

urlpatterns = [
    path('', inicio),
    path('Post/', post),
]
