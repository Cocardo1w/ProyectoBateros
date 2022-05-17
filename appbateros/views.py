from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post(request):
    return render(request,"appbateros/Post.html")
    

def inicio(request):
    return render(request, "appbateros/index.html")
