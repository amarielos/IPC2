from django.shortcuts import render
from gestionDatos.models import *

def inicio(request):
    return render(request, 'inicio.html')

def usuarios(request):
    no_usuarios = Usuarios.objects.count()
    usuarios_var = Usuarios.objects.all()
    return render(request, 'usuarios.html', {'No_usuarios' :no_usuarios, 'Usuarios': usuarios_var})
