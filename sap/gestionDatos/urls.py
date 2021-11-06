from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import*

urlpatterns = [
    path('home/', home, name='home'),

    path('empresa/', empresa, name='empresa'),
    path('agregar-empresa/', agregar_empresa, name='agregar_empresa'),
    path('modificar-empresa/<id>/', modificar_empresa, name='modificar_empresa'),
    path('eliminar-empresa/<id>/', eliminar_empresa, name='eliminar_empresa'),

    path('evento/', evento, name='evento'),
    path('agregar-evento',agregar_evento, name='agregar_evento'),

    path('producto/', producto, name='producto'),
    path('agregar-producto',agregar_producto, name='agregar_producto'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),

    path('tarea/', tarea, name='tarea'),
    path('agregar-tarea', agregar_tarea, name='agregar_tarea'),

    path('contacto/', contacto, name='contacto'),
    path('agregar-contacto/', agregar_contacto, name='agregar_contacto'),
    path('modificar-contacto/<id>/', modificar_contacto, name="modificar_contacto"),
    path('eliminar-contacto/<id>/', eliminar_contacto, name="eliminar_contacto"),

    path('usuario/', usuario, name='usuario'),
    path('agregar-usuario', agregar_usuario, name='agregar_usuario'),
    path('modificar-usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    path('eliminar-usuario/<id>/', eliminar_usuario, name="eliminar_usuario"),
    path('trato/', trato, name ='trato'),
    path('agregar-trato', agregar_trato, name='agregar_trato'),
]