from django.db import models
from django.contrib.auth.models import User
import os
#from location_field.models.plain import PlainLocationField

# Create your models here.
def get_upload_path_Perfil(instance, filename):	#retorna direccion para las imagenes
    return os.path.join(
      "image/Perfiles/fotos/usuario_%d" % instance.id, filename)

def get_upload_path_Inmueble(instance, filename):	#retorna direccion para las imagenes
    return os.path.join(
      "image/Inmueble/inmueble_%d" % instance.id, filename)

class Usuario(models.Model):
	cedula = models.CharField(max_length=30, unique=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	telefono = models.CharField(max_length=20, null=True, blank=True)
	celular = models.CharField(max_length=20, null=True, blank=True)
	foto = models.ImageField(upload_to=get_upload_path_Perfil, null=True, blank=True)
	activo = models.BooleanField(default=True)
	fecha_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)					#usuario que ingreso registro
	def __unicode__(self):	
		return self.cedula

class Inmueble(models.Model):
	tipo = models.CharField(max_length=50)	#tipo
	numero_habitaciones = models.CharField(max_length=40, null=True, blank=True)
	ubicacion = models.CharField(max_length=100, null=True, blank=True)
	ciudad = models.CharField(max_length=80, null=True, blank=True)
	descripcion = models.TextField(null=True,blank=True)
	valor = models.CharField(max_length=20, null=True, blank=True)
	estrato = models.CharField(max_length=20, null=True, blank=True)
	para = models.CharField(max_length=20, null=True, blank=True)
	foto1 = models.ImageField(upload_to=get_upload_path_Inmueble, null=True, blank=True)
	foto2 = models.ImageField(upload_to=get_upload_path_Inmueble, null=True, blank=True)
	foto3 = models.ImageField(upload_to=get_upload_path_Inmueble, null=True, blank=True)
	foto4 = models.ImageField(upload_to=get_upload_path_Inmueble, null=True, blank=True)
	activo = models.BooleanField(default=True)
	fecha_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)					#usuario que ingreso registro
	def __unicode__(self):	
		return self.id_presupuesto

class FotoInmueble(models.Model):
	inmueble = models.ForeignKey(Inmueble)
	foto = models.ImageField(upload_to=get_upload_path_Inmueble, null=True, blank=True)