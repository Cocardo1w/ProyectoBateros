from django.http import HttpResponse
from django.shortcuts import render
from appbateros.forms import ComentarioForm
from appbateros.models import Autor, Categoria, Post, Comentario
from appbateros.forms import ComentarioForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
    
def inicio(request):
    return render(request, "appbateros/index.html")

def base(request):
    posts = Post.objects.filter(estado = True) #Post es el models
    return render(request, "appbateros/base.html")

def Inicio(request):
    return render(request, "appbateros/Inicio.html")

def post(request):
    articulos = Post.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            comentario= form.cleaned_data['comentario']
            obj = Comentario(nombre=nombre, comentario=comentario)
            obj.save()
            form = ComentarioForm() #genera formulario
            mensaje = "Gracias por tu comentario"
            return render(request,"appbateros/Post.html", {"articulos":articulos, "mensaje": mensaje, "form": form})
    form = ComentarioForm()
    return render(request, "appbateros/Post.html", {'articulos': articulos, "form": form})


def partituras(request):
        
    return render(request, "appbateros/partituras.html")
       
def about(request):
    return render(request, "appbateros/about.html")

def contacto(request):
    return render(request, "appbateros/contacto.html")


def login_request(request):

    if request.method == "POST": #validando que es post...
        form = AuthenticationForm(request, data = request.POST) #creamos el formulario

        if form.is_valid(): # pregunto si es valido
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "appbateros/base.html", {"mensaje":f"Bienvenido {usuario}"} )
            else:
                return render(request, "appbateros/base.html", {"mensaje":f"Error, datos incorrectos "})

        else:
                return render(request, "appbateros/base.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request, "appbateros/login.html", {'form': form})

def register_request(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("Nombre de Usuario")
            form.save() # guarda los datos del modelo del usuario

            dict_ctx = {"title": "Inicio", "page": usuario}
            return render(request, "appbateros/index.html", dict_ctx)        
        else:
            dict_ctx = {"title": "Inicio", "page": "anonimos", "errors": ["no pasó las validaciones"] }
            return render(request, "appbateros/base.html", dict_ctx)
    else:
        form = UserCreationForm()
        return render(request, "appbateros/register.html", {"form": form})











