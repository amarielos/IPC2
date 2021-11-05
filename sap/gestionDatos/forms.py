from django import forms
from .models import *


class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        #fields = []
        fields = '__all__'


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = []
        fields = '__all__'


class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        #fields = []
        fields = '__all__'


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        #fields = []
        fields = '__all__'


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        #fields = []
        fields = '__all__'


class TratoForm(forms.ModelForm):

    class Meta:
        model = Trato
        #fields = []
        fields = '__all__'


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        #fields = []
        fields = '__all__'