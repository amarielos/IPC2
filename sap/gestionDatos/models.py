from django.db import models
from .choices import activo

# Create your models here.
class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_emp = models.CharField(unique=True, max_length=50, verbose_name="Nombre")
    tlfn_emp = models.CharField(max_length=8, verbose_name="Teléfono") # verbose_name: nombre del campo
    sitio_web = models.CharField(max_length=50)
    descrip_emp = models.CharField(max_length=100, verbose_name="Descripción")
    domicilio = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=25, blank=True, null=True)
    pais = models.CharField(max_length=25, blank=True, null=True)
    codigoPostal = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.nombre_emp}: {self.tlfn_emp} {self.sitio_web} {self.descrip_emp} '\
                f'{self.domicilio} {self.ciudad} {self.departamento} {self.pais} {self.codigoPostal}'



# blank=True, null=True para permitir espacios vacios
class Contacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_cont = models.CharField(max_length=50, verbose_name="Nombre")
    apellido_cont = models.CharField(unique=True, max_length=50, verbose_name="Apellido")
    titulo_contacto = models.CharField(max_length=50, verbose_name="Título")
    email_cont = models.EmailField()
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True) # id de empresa
    movil_cont = models.CharField(max_length=8, verbose_name="Móvil")
    tlfn_cont = models.CharField(max_length=8, verbose_name="Teléfono", blank=True, null=True)
    tlfn_casa = models.CharField(max_length=8, verbose_name="Teléfono de casa", blank=True, null=True)
    email_opt_out = models.BooleanField() #editar todavia
    descrip_cont = models.CharField(max_length=100, verbose_name="Descripción", blank=True, null=True)

    def __str__(self):
        return f'Contacto {self.id} {self.apellido_cont} {self.nombre_cont} {self.titulo_contacto} {self.email_cont} {self.empresa} {self.movil_cont} {self.tlfn_cont} {self.tlfn_casa} {self.email_opt_out} {self.descrip_cont}'


class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_prod = models.CharField(unique=True, max_length=50)
    cod_prod = models.CharField(unique=True, max_length=5)
    categ_prod = models.CharField(max_length=20)
    precio_uni = models.IntegerField()
    descrip_prod = models.CharField(max_length=100)
    prod_act = models.CharField(max_length=1, choices=activo, default='S') # choices para escribir si está activo o no el producto

    def __str__(self):
        return f'Producto {self.id} {self.nombre_prod} {self.cod_prod} {self.categ_prod} {self.precio_uni} {self.descrip_prod} {self.prod_act}'


class Usuario(models.Model):
    us_name = models.CharField(max_length=50)
    us_lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    us_password = models.CharField(max_length=15)#verificar
    us_email = models.EmailField()
    us_phone = models.CharField(max_length=8)

    def __str__(self):
        return f'Usuario {self.id}: {self.us_name} {self.us_lastname} {self.username} {self.username} {self.us_email}' \
               f' {self.us_phone} '


class Tarea(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(unique=True, max_length=50)
    task_duedate = models.DateField()
    repeat = models.BooleanField(default=False)
    relatedTo = models.ForeignKey(Contacto, on_delete=models.SET_NULL, null=True)#agregar empresa y deals
    description = models.CharField(max_length=100)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return f'Tarea {self.id}: {self.task_name} {self.task_duedate} {self.repeat} {self.relatedTo} ' \
               f'{self.description} {self.priority}'


class Evento(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=50)
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
    id = models.BigAutoField(primary_key=True)
    trato_nombre = models.CharField(unique=True, max_length=50)
    contacto_nombre = models.ForeignKey(Contacto, on_delete=models.SET_NULL, null=True)
    empresa_nombre = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    estado = models.IntegerField(choices=estados)
    cant = models.FloatField()
    fechacierre = models.DateField()
    descripcion = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Trato {self.id}: {self.trato_nombre} {self.contacto_nombre} {self.empresa_nombre} {self.estado} {self.cant} ' \
               f'{self.fechacierre} {self.descripcion} {self.producto}'


