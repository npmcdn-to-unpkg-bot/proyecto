from django.shortcuts import render
from caja.models import Cliente,CajaAhorros,CuentaAhorros,Transaccion
from rest_framework import  viewsets
from .serializable import ClienteSerializable, CajaAhorros_Serializable, CuentaAhorros_Serializable,Transaccion_Serializable

class ClienteViewSet(viewsets.ModelViewSet):
	#objeto serialiable->transforma para enviarlo por la red en cualquier archivo
	serializer_class = ClienteSerializable
	#se define la consulta de datos 
	queryset = Cliente.objects.all().order_by('apellidos')

class CajaAhorrosViewSet(viewsets.ModelViewSet):
	serializer_class = CajaAhorros_Serializable
	queryset = CajaAhorros.objects.all()
	
class CuentaAhorrosViewSet(viewsets.ModelViewSet):
	serializer_class = CuentaAhorros_Serializable
	queryset = CuentaAhorros.objects.all()

class TransaccionViewSet(viewsets.ModelViewSet):
	serializer_class = Transaccion_Serializable
	queryset = Transaccion.objects.all()

