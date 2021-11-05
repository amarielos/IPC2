from django.shortcuts import render
from gestionDatos.models import *

def detalleUser(request, id):
    usuario = Usuarios.objects.get(pk=id)
    return render(request, 'gestionDatos/detalleUser.html', {'Usuario': usuario})
