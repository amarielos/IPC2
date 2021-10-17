from django.db import models


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
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    sitio_web = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Empresa {self.id}: {self.nombre} {self.telefono} {self.sitio_web} {self.descripcion}'
