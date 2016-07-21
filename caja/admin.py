from django.contrib import admin
from .models import CajaAhorros, Cliente,CuentaAhorros

# Register your models here.

class AdmCajaAhorros(admin.ModelAdmin):
	list_display = ["__str__","nombre","siglas","logo"]
	class Meta:
		model = CajaAhorros
admin.site.register(CajaAhorros,AdmCajaAhorros)
 
class AdmCliente(admin.ModelAdmin):
	list_display = ["__str__","nombres","apellidos","correo","telefono","celular","direccion","genero","estadoCivil","fechaNacimiento"]
	class Meta:
		model = Cliente
admin.site.register(Cliente,AdmCliente)	

class AdmCuentaAhorros(admin.ModelAdmin):
	list_display = ["__str__","numeroCuenta","cliente","estado","fechaApertura","saldo"]
	class Meta:
		model = CuentaAhorros
admin.site.register(CuentaAhorros,AdmCuentaAhorros)