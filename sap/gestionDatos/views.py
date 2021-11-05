from django.shortcuts import render
from .models import *
from .forms import EmpresaForm

def detalleUser(request, id):
    usuario = Usuarios.objects.get(pk=id)
    return render(request, 'gestionDatos/detalleUser.html', {'Usuario': usuario})

def home(request):
    return render(request, 'gestionDatos/home.html')

def contacto(request):
    return render(request, 'gestionDatos/contacto.html')

def producto(request):
    return render(request, 'gestionDatos/producto.html')

def tarea(request):
    return render(request, 'gestionDatos/tarea.html')

def usuario(request):
    usuarios = Usuarios.objects.all()
    data = {
        'usuarios': usuarios
    }
    return render(request, 'gestionDatos/usuario.html', data)

def evento(request):
    return render(request, 'gestionDatos/evento.html')

def agregar_empresa(request):
    data = {
        'form': EmpresaForm
    }

    if request.method == 'POST':
        formulario = EmpresaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']= 'Empresa añadida'

        else:
            data['form']= formulario

    return render(request, 'gestionDatos/empresa/agregar.html', data)

def empresa(request):
    empresas = Empresa.objects.all()
    data = {
        'empresas': empresas
    }
    return render(request, 'gestionDatos/empresa.html', data)

def modificar_empresa(request, nombre): #falta
    empresa = get_object_or_404(Empresa, nombre_emp=nombre)

    data = {
        'form': EmpresaForm(instance=empresa)
    }

    return render(request, 'gestionDatos/empresa/modificar.html', data)

def trato(request):
    return render(request, 'gestionDatos/trato.html')