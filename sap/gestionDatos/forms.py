from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        #fields = []
        fields = '__all__'
