from django import forms
from .models import Cliente, CuentaAhorros, Transaccion

class Formulario(forms.Form):
	nombre = forms.CharField(max_length=30)
	siglas = forms.CharField(max_length=10)
	logo = forms.CharField(max_length=20)
	
class Formulario_Crear(forms.ModelForm):	
	class Meta:
		model = Cliente
		fields = ["nombres","apellidos","cedula","correo","telefono","celular","direccion","genero","estadoCivil","fechaNacimiento"]

class Formulario_Modificar(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ["nombres","apellidos","cedula","correo","telefono","celular","direccion","genero","estadoCivil","fechaNacimiento"]

class Formulario_Eliminar(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ["cedula"]

class Formulario_Cliente_M(forms.ModelForm):	
	class Meta:
		model = Cliente
		fields = ["nombres","apellidos","correo","telefono","celular","direccion","genero","estadoCivil","fechaNacimiento"]

class Formulario_usuario(forms.Form):
	username = forms.CharField(max_length=20)	
	password = forms.CharField(max_length=20)

class Formulario_Transaccion(forms.ModelForm):
	class Meta:
		model = Transaccion
		fields = ["descripcion","tipo","valor"]

class Formulario_Cuenta_Ahorros(forms.ModelForm):
    class Meta:
        model = CuentaAhorros
        fields= ["saldo"]
