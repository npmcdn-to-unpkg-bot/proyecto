#transformar los objetos y dar propiedades para que se puedan represetar en otros formatos

from rest_framework import serializers
from caja.models import Cliente,CajaAhorros, CuentaAhorros, Transaccion

class ClienteSerializable(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = ("cedula","nombres","apellidos","correo","telefono","celular","direccion","genero","estadoCivil","fechaNacimiento")

class CajaAhorros_Serializable(serializers.ModelSerializer):
	class Meta:
		model = CajaAhorros
		fields = ("nombre","siglas")

class CuentaAhorros_Serializable(serializers.ModelSerializer):
	class Meta:
		model = CuentaAhorros
		fields = ("numeroCuenta","estado","fechaApertura","saldo")

class Transaccion_Serializable(serializers.ModelSerializer):
	class Meta:
		model = Transaccion
		fields = ("fecha","descripcion","tipo","valor")