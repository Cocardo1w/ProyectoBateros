from django.http import HttpResponse

from django.shortcuts import render, redirect

from appbateros.forms import ComentarioForm, UsuarioEditForm
from appbateros.models import Autor, Categoria, Post, Comentario, Liked
from django.db.models.query import QuerySet

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
    
def inicio(request):
    return render(request, "appbateros/index.html")

def base(request):
    posts = Post.objects.filter(estado = True) #Post es el models
    return render(request, "appbateros/base.html")


def post(request):
    articulos = Post.objects.all().order_by('fecha_creacion')
    comentarios = Comentario.objects.all()
    context = like = 'like'
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            comentario= form.cleaned_data['comentario']
            obj = Comentario(nombre=nombre, comentario=comentario)
            obj.save()
            form = ComentarioForm() #genera formulario
            mensaje = "Gracias por tu comentario"
            
            return render(request,"appbateros/Post.html", {"articulos":articulos, "mensaje": mensaje, "form": form, 'comentarios': comentarios, "like": like})
    form = ComentarioForm()
    return render(request, "appbateros/Post.html", {'articulos': articulos, "form": form, 'comentarios': comentarios, "like": like})

def BorrarPost(request, id):
    try:
        p = Post.objects.get(id=id)
        p.delete()

        return render(request, "appbateros/index.html")
    except Exception as exc:
        return render(request, "appbateros/index.html")

def LikedPost(request):
    user = request.user

    if request.method == 'POST':
        post.id = request.POST.get('post.id')
        
    

def libros(request):        
    return render(request, "appbateros/libros.html")

def DrumsDoctor(request):
    return render (request,"appbateros/drumsdoctor.html")
       
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
            # usuario = form.cleaned_data.get SEGUIR !!!
            dict_ctx = {"title": "Inicio", "page": usuario}
            return render(request, "appbateros/index.html", dict_ctx)        
        else:
            dict_ctx = {"title": "Inicio", "page": "anonimos", "errors": ["no pasó las validaciones"] }
            return render(request, "appbateros/base.html", dict_ctx)
    else:
        form = UserCreationForm()
        return render(request, "appbateros/register.html", {"form": form})

@login_required()
def actualizar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        formulario = UsuarioEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.last_name = data["last_name"]
            usuario.first_name = data["first_name"]

            usuario.save()

            return redirect("Inicio")
        else:
            formulario = UsuarioEditForm(initial={"email": usuario.email})
            return render(request, "appbateros/editar_usuario.html", {"form": formulario, "errors": ["Datos invalidos"]})

    else:
        formulario = UsuarioEditForm(initial={"email": usuario.email})
        return render(request, "appbateros/editar_usuario.html", {"form": formulario})

def BancoMusicos(request):
    return render(request, "appbateros/Bancomusicos.html")

def Clases(request):
    return render(request, "appbateros/clases.html")











