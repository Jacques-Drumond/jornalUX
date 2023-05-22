from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(request):
    try:
        return HttpResponse("Funcionando")
    except:
        return HttpResponseNotFound("Não funcionou")