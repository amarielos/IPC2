from django.shortcuts import render
from gestionDatos.models import *

def inicio(request):
    return render(request, 'inicio.html')

def usuarios(request):
    no_usuarios = Usuario.objects.count()
    usuarios_var = Usuario.objects.all()
    return render(request, 'usuarios.html', {'No_usuarios' :no_usuarios, 'Usuarios': usuarios_var})
