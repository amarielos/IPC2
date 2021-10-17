from django.db import models
from .choices import activo

# Create your models here.

class Domicilio(models.Model):
    domicilio = models.CharField(max_length=50)  # domicilio de correspondencia
    ciudad = models.CharField(max_length=50)
    departamento = models.CharField(max_length=25)
    pais = models.CharField(max_length=25)
    codigoPostal = models.CharField(max_length=10)

    def __str__(self):
        return f'Dirección {self.id}: {self.domicilio} {self.ciudad} {self.departamento} {self.pais} {self.codigoPostal}'


class Empresa(models.Model):
    nombre_emp = models.CharField(primary_key=True, max_length=50)
    tlfn_emp = models.CharField(max_length=8)
    sitio_web = models.CharField(max_length=50)
    descrip_emp = models.CharField(max_length=100)
    domicilio_emp = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Empresa {self.nombre_emp}: {self.tlfn_emp} {self.sitio_web} {self.descrip_emp} {self.domicilio_emp}'

class Contacto(models.Model):
    nombre_cont = models.CharField(max_length=50)
    apellido_cont = models.CharField(primary_key=True, max_length=50)
    titulo_contacto = models.CharField(max_length=50)
    email_cont = models.EmailField()
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True) # id de empresa
    movil_cont = models.CharField(max_length=8)
    tlfn_cont = models.CharField(max_length=8)
    tlfn_casa = models.CharField(max_length=8)
    email_opt_out = models.CharField(max_length=10) #editar todavia
    descrip_cont = models.CharField(max_length=100)

    def __str__(self):
        return f'Contacto {self.apellido_cont}: {self.nombre_cont} {self.titulo_contacto} {self.email_cont} {self.empresa} {self.movil_cont} {self.tlfn_cont} {self.tlfn_casa} {self.email_opt_out} {self.descrip_cont}'

class Producto(models.Model):
    nombre_prod = models.CharField(primary_key=True, max_length=50)
    cod_prod = models.CharField(unique=True, max_length=5)
    categ_prod = models.CharField(max_length=20)
    precio_uni = models.IntegerField()
    descrip_prod = models.CharField(max_length=100)
    prod_act = models.CharField(max_length=1, choices=activo, default='S') # choices para escribir si está activo o no el producto

    def __str__(self):
        return f'Producto {self.nombre_prod}: {self.cod_prod} {self.categ_prod} {self.precio_uni} {self.descrip_prod} {self.prod_act}'

