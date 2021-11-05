from django.urls import path
from .views import home, contacto, empresa, evento,producto, tarea, usuario, trato, agregar_empresa, modificar_empresa

urlpatterns = [
    path('home/', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('empresa/', empresa, name='empresa'),
    path('evento/', evento, name='evento'),
    path('producto/', producto, name='producto'),
    path('tarea/', tarea, name='tarea'),
    path('usuario/', usuario, name='usuario'),
    path('trato/', trato, name ='trato'),
    path('agregar-empresa/', agregar_empresa, name='agregar_empresa'),
    path('modificar-empresa/<nombre>/', modificar_empresa, name='modificar_empresa'),
]