from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    activo = models.BooleanField(default=False)
### Se agrego la variable "activo" para que al habilitar o deshabilitar un vehiculo, quedara registro visible en la base de datos"   
class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo_id = models.OneToOneField(Vehiculo, null=True, on_delete=models.CASCADE)

class Registro_contabilidad(models.Model):
    fecha_compra = models.DateField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    vehiculo_id = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)

    
