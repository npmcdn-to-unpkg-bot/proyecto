from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contacto(models.Model):
	nombres = models.CharField(max_length=30,blank=True)
	apellidos = models.CharField(max_length=30)
	cedula = models.CharField(max_length=10)
	email = models.EmailField()
	#edad = models.IntegerField()

	# para python 3
	#def _str_(self):
	#	pass 

	#para python 2.7
	def __str__(self):
		return str(self.email)

class Info(models.Model):
	direccion = models.CharField(max_length=30) 
	telefono = models.CharField(max_length=30,blank=True)

	def __str__(self):
		return str(self.direccion)