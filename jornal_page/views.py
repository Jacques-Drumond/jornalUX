from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
# Create your views here.

def index(request):
    try:
        pdf_file = open(r"C:\Users\jacques.drumond\Desktop\jornal\_New Ux Times Abril (1).pdf", "rb")
        return FileResponse(pdf_file, content_type='application/pdf')
    except:
        return HttpResponseNotFound("Não funcionou")