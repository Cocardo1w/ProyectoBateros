from django.http import HttpResponse
from django.shortcuts import render
from appbateros.models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def post(request):
    return render(request,"appbateros/Post.html")
    

def inicio(request):
    return render(request, "appbateros/index.html")

def base(request):
    return render(request, "appbateros/base.html")


def partituras(request):
        
    return render(request, "appbateros/partituras.html")
       
    


def blog(request):

    articulos = Blog.objects.all()
             
        
    return render(request, "appbateros/index.html", {"articulos": articulos}) 

def contacto(request):
    return render(request, "appbateros/contacto.html")


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
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

