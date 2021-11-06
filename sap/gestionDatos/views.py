from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def home(request):
    return render(request, 'gestionDatos/home.html')


# contacto----------------------------------------------------------------------------------------------------------
def contacto(request):
    contactos = Contacto.objects.all()
    data = {
        'contactos': contactos
    }
    return render(request, 'gestionDatos/contacto.html', data)


def buscar_contacto(request):
    busqueda = request.POST.get("buscar")
    contacto = Contacto.objects.all()

    if busqueda:
        contacto = Contacto.objects.filter(
            Q(nombre_cont__icontains=busqueda) |
            Q(apellido_cont__icontains=busqueda) |
            Q(titulo_contacto__icontains=busqueda) |
            Q(descrip_cont__icontains=busqueda)
        ).distinct()

    return render(request, 'contacto.html', {'contacto': contacto})


def agregar_contacto(request):
    data = {
        'form': ContactoForm
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Contacto añadido'

        else:
            data['form'] = formulario

    return render(request, 'gestionDatos/contacto/agregar.html', data)

def modificar_contacto(request, id):  # falta
    contacto= get_object_or_404(Contacto, nombre_cont=id)

    data = {
        'form': ContactoForm(instance=contacto)
    }

    if request.method ==  'POST':
        formulario = ContactoForm(data=request.POST, instance=contacto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="contacto")
        data["form"]=formulario

    return render(request, 'gestionDatos/contacto/modificar.html', data)

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect(to="contacto")


# Producto-------------------------------------------------------------------------------------------------------------
def producto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'gestionDatos/producto.html', data)


def agregar_producto(request):
    data = {
        'form': ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Producto añadido'

        else:
            data['form'] = formulario

    return render(request, 'gestionDatos/empresa/agregar.html', data)

def modificar_producto(request, id):  # falta
    producto= get_object_or_404(Contacto, nombre_prod=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method ==  'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="producto")
        data["form"]=formulario

    return render(request, 'gestionDatos/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="producto")


# Tarea---------------------------------------------------------------------------------------------------------------
def tarea(request):
    tareas = Tarea.objects.all()
    data = {
        'tareas': tareas
    }
    return render(request, 'gestionDatos/tarea.html', data)


def agregar_tarea(request):
    data = {
        'form': TareaForm
    }

    if request.method == 'POST':
        formulario = TareaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Tarea añadida'

        else:
            data['form'] = formulario

    return render(request, 'gestionDatos/empresa/agregar.html', data)

def modificar_tarea(request, id):  # falta
    tarea = get_object_or_404(Tarea, nombre_emp=id)

    data = {
        'form': TareaForm(instance=tarea)
    }

    if request.method ==  'POST':
        formulario = TareaForm(data=request.POST, instance=tarea, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="tarea")
        data["form"]=formulario

    return render(request, 'gestionDatos/tarea/modificar.html', data)


def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect(to="tarea")


# Usuario--------------------------------------------------------------------------------------------------------------
def usuario(request):
    usuarios = Usuario.objects.all()
    data = {
        'usuarios': usuarios
    }
    return render(request, 'gestionDatos/usuario.html', data)


def agregar_usuario(request):
    data = {
        'form': UsuarioForm
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Usuario añadido'

        else:
            data['form'] = formulario

    return render(request, 'gestionDatos/usuario/agregar.html', data)


def modificar_usuario(request, id):  # falta
    usuario = get_object_or_404(Usuario, us_name=id)

    data = {
        'form': UsuarioForm(instance=usuario)
    }

    if request.method ==  'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="usuario")
        data["form"]=formulario

    return render(request, 'gestionDatos/usuario/modificar.html', data)

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()
    return redirect(to="usuario")


def detalleUser(request, id):
    usuario = Usuario.objects.get(pk=id)
    return render(request, 'gestionDatos/detalleUser.html', {'Usuario': usuario})


# Evento---------------------------------------------------------------------------------------------------------------
def evento(request):
    eventos = Evento.objects.all()
    data = {
        'eventos': eventos
    }
    return render(request, 'gestionDatos/evento.html', data)


def agregar_evento(request):
    data = {
        'form': EventoForm
    }

    if request.method == 'POST':
        formulario = EventoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Evento añadido'

        else:
            data['form'] = formulario

    return render(request, 'gestionDatos/empresa/agregar.html', data)


# Empresa--------------------------------------------------------------------------------------------------------------
def empresa(request):
    empresas = Empresa.objects.all()
    data = {
        'empresas': empresas
    }
    return render(request, 'gestionDatos/empresa.html', data)


def buscar_empresa(request):
    busqueda = request.GET.get("buscar")
    empresa = Empresa.objects.all()

    if busqueda:
        empresa = Empresa.objects.filter(
            Q(nombre_emp__icontains = busqueda)
        ).distinct()

    return render(request, 'empresa.html', {'empresa': empresa})


def agregar_empresa(request):
    data = {
        'form': EmpresaForm
    }

    if request.method == 'POST':
        formulario = EmpresaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Empresa añadida'

        else:
            data['form'] = formulario

    return render(request, 'gestionDatos/empresa/agregar.html', data)

def modificar_empresa(request, id):  # falta
    empresa = get_object_or_404(Empresa, nombre_emp=id)

    data = {
        'form': EmpresaForm(instance=empresa)
    }

    if request.method ==  'POST':
        formulario = EmpresaForm(data=request.POST, instance=empresa, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="empresa")
        data["form"]=formulario

    return render(request, 'gestionDatos/empresa/modificar.html', data)


def eliminar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    empresa.delete()
    return redirect(to="empresa")

# Trato---------------------------------------------------------------------------------------------------------------
def trato(request):
    tratos = Trato.objects.all()
    data = {
        'tratos': tratos
    }
    return render(request, 'gestionDatos/trato.html', data)


def agregar_trato(request):
    data = {
        'form': TratoForm
    }

    if request.method == 'POST':
        formulario = TratoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Trato añadido'

        else:
            data['form'] = formulario

    return render(request, 'gestionDatos/empresa/agregar.html', data)


def modificar_trato(request, id):  # falta
    trato = get_object_or_404(Trato, us_name=id)

    data = {
        'form': TratoForm(instance=trato)
    }

    if request.method ==  'POST':
        formulario = TratoForm(data=request.POST, instance=trato, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="trato")
        data["form"]=formulario

    return render(request, 'gestionDatos/trato/modificar.html', data)

def eliminar_trato(request, id):
    trato = get_object_or_404(Trato, pk=id)
    trato.delete()
    return redirect(to="trato")