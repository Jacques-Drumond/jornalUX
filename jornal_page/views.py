from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
# Create your views here.

def jornal(request):
    try:
        pdf_file = open(r"C:\Users\jacques.drumond\Desktop\jornal\_New Ux Times Abril (1).pdf", "rb")
        return FileResponse(pdf_file, content_type='application/pdf')
    except:
        return HttpResponseNotFound("Não funcionou")


def index(request):
    return render(request, "jornal_page/index.html")