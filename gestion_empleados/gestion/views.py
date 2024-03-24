from django.shortcuts import render
from django.http import HttpResponse
from .models import Salarios
# Create your views here.
def index(request):

    return render(request,'index.html',{})

def salarios(request):

    return render(request, 'salary.html',{})

def save (request):
    amount = request.get["amount"]
    return HttpResponse('hola')