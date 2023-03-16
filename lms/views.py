from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def cards(request):
    return render(request, 'cards-basic.html')

def aboutDetails(request, id):
    return HttpResponse(id)