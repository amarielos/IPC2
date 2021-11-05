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
    nombre_emp = models.CharField(primary_key=True, max_length=50, verbose_name="Nombre")
    tlfn_emp = models.CharField(max_length=8, verbose_name="Teléfono") # verbose_name: nombre del campo
    sitio_web = models.CharField(max_length=50)
    descrip_emp = models.CharField(max_length=100, verbose_name="Descripción")
    domicilio_emp = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Empresa {self.nombre_emp}: {self.tlfn_emp} {self.sitio_web} {self.descrip_emp} {self.domicilio_emp}'

# blank=True, null=True para permitir espacios vacios
class Contacto(models.Model):
    nombre_cont = models.CharField(max_length=50, verbose_name="Nombre")
    apellido_cont = models.CharField(primary_key=True, max_length=50, verbose_name="Apellido")
    titulo_contacto = models.CharField(max_length=50, verbose_name="Título")
    email_cont = models.EmailField()
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True) # id de empresa
    movil_cont = models.CharField(max_length=8, verbose_name="Móvil")
    tlfn_cont = models.CharField(max_length=8, verbose_name="Teléfono")
    tlfn_casa = models.CharField(max_length=8, verbose_name="Teléfono de casa")
    email_opt_out = models.CharField(max_length=10) #editar todavia
    descrip_cont = models.CharField(max_length=100, verbose_name="Descripción")

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


class Usuarios(models.Model):
    us_name = models.CharField(max_length=50)
    us_lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    us_password = models.CharField(max_length=15)#verificar
    us_email = models.EmailField()
    us_phone = models.CharField(max_length=8)

    def __str__(self):
        return f'Usuario {self.id}: {self.us_name} {self.us_lastname} {self.username} {self.username} {self.us_email}' \
               f' {self.us_phone} '


class Task(models.Model):
    task_name = models.CharField(primary_key=True, max_length=50)
    task_duedate = models.DateField()
    repeat = models.BooleanField(default=False)
    relatedTo = models.ForeignKey(Contacto, on_delete=models.SET_NULL, null=True)#agregar empresa y deals
    description = models.CharField(max_length=100)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return f'Tarea {self.id}: {self.task_name} {self.task_duedate} {self.repeat} {self.relatedTo} ' \
               f'{self.description} {self.priority}'


class Event(models.Model):
    title = models.CharField(primary_key=True, max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    repeat = models.BooleanField(default=False)
    location = models.CharField(max_length=50)
    relatedTo = models.ForeignKey(Contacto, on_delete=models.SET_NULL, null=True)#agregar empresa y deals
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'Evento {self.id}: {self.title} {self.from_date} {self.to_date} {self.repeat} {self.relatedTo} ' \
               f'{self.description}'


estados = [
    [0, "Clasificación"],
    [1, "Dimensionamiento"],
    [2, "Cotización de propuesta/precio"],
    [3, "Negociación/revisión"],
    [4, "Facturado"],
    [5, "Pagado"],
    [6, "Cerrado ganado"],
    [7, "Cerrado perdido"]
]


class Trato(models.Model):
    trato_nombre = models.CharField(primary_key=True, max_length=50)
    cont_nombre = models.ForeignKey(Contacto, on_delete=models.SET_NULL, null=True)
    emp_nombre = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    estado = models.IntegerField(choices=estados)
    cant = models.FloatField()
    fechacierre = models.DateField()
    desc = models.CharField(max_length=100)
    prod = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)



