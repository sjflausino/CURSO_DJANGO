from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'global/home.html', context={'name':'Sandor Clegane',})

def contato(request):
    return HttpResponse("CONTATO 1 ")

def sobre(request):
    return HttpResponse("SOBRE! 1")
