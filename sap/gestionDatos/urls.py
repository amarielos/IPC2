from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import*

urlpatterns = [
    path('home/', home, name='home'),

    path('contacto/', contacto, name='contacto'),
    path('agregar-contacto/', agregar_contacto, name='agregar_contacto'),
    path('contacto/', login_required(buscar_contacto), name='contacto'),

    path('empresa/', evento, name='empresa'),
    path('agregar-empresa/', agregar_empresa, name='agregar_empresa'),
    path('empresa/', buscar_empresa, name='empresa'),
    path('modificar-empresa/<nombre>/', modificar_empresa, name='modificar_empresa'),

    path('evento/', evento, name='evento'),
    path('agregar-evento',agregar_evento, name='agregar_evento'),

    path('producto/', producto, name='producto'),
    path('agregar-producto',agregar_producto, name='agregar_producto'),

    path('tarea/', tarea, name='tarea'),
    path('agregar-tarea', agregar_tarea, name='agregar_tarea'),

    path('usuario/', usuario, name='usuario'),
    path('agregar-usuario', agregar_usuario, name='agregar_usuario'),

    path('trato/', trato, name ='trato'),
    path('agregar-trato', agregar_trato, name='agregar_trato'),
]