from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CajaAhorros(models.Model):
	nombre = models.CharField(max_length=30)
	siglas = models.CharField(max_length=10)
	logo = models.FilePathField(max_length=20,blank=True,null=True)
	#direccion = models.CharField(max_length=30)
	#telefono = models.CharField(max_length=15)

	def __str__(self):
		return str(self.nombre)

class Cliente(models.Model):
	
	listaGenero = {
		('femenino','femenino'),
		('masculino','masculino'),
	}
	listaEC = {
		('soltero','soltero'),
		('casado','casado'),
		('divorciado','divorciado'),
		('viudo','viudo'),
	}
	idCA = models.ForeignKey(CajaAhorros,on_delete=models.CASCADE,default="")
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	cedula = models.CharField(max_length=10)
	correo = models.EmailField(max_length=30,blank=True,null=True)
	telefono = models.CharField(max_length=15,blank=True,null=True)
	celular = models.CharField(max_length=15,blank=True,null=True) 
	direccion = models.TextField(max_length=10,default="direccion")
	genero = models.CharField(max_length=10, choices=listaGenero)
	estadoCivil = models.CharField(max_length=10, choices=listaEC)
	fechaNacimiento = models.DateField(blank=True,null=True)

	def __str__(self):
		return str(self.cedula)

class CuentaAhorros(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,default="")
	numeroCuenta = models.CharField(max_length=20)
	estado = models.BooleanField()
	fechaApertura = models.DateTimeField(auto_now=True, auto_now_add=False)
	saldo = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return str(self.numeroCuenta)

class Transaccion(models.Model):
	listatrans = {
		('deposito','deposito'),
		('retiro','retiro'),
	}
	idCuenta = models.ForeignKey(CuentaAhorros, on_delete=models.CASCADE,default="")
	fecha = models.DateTimeField(auto_now=True, auto_now_add=False)
	descripcion = models.TextField(max_length=50,default="descripcion")
	tipo = models.CharField(max_length=30, choices=listatrans)
	valor = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)

	def __str__(self):
		return str(self.idCuenta)