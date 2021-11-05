from django.shortcuts import render
from gestionDatos.models import *


def inicio(request):
    return render(request, 'inicio.html')
