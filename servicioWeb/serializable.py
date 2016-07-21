#transformar los objetos y dar propiedades para que se puedan represetar en otros formatos

from rest_framework import serializers
from caja.models import Cliente,CajaAhorros, CuentaAhorros

class ClienteSerializable(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = ("cedula","nombres","apellidos")

class CajaAhorros_Serializable(serializers.ModelSerializer):
	class Meta:
		model = CajaAhorros
		fields = ("nombre","siglas")

class CuentaAhorros_Serializable(serializers.ModelSerializer):
	class Meta:
		model = CuentaAhorros
		fields = ("numeroCuenta","estado","fechaApertura","saldo")