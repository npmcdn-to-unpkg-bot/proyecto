from django import forms
from .models import Contacto

class Formulario(forms.Form):
	nombres = forms.CharField(max_length=30)
	apellidos = forms.CharField(max_length=30)
	cedula = forms.CharField(max_length=10)
	email = forms.EmailField()
	#edad = forms.IntegerField()

class FormularioModelo(forms.Form):
	class Meta:
		model = Contacto
		fields = ["nombres","apellidos","cedula","email"]

class FormularioModeloA(forms.ModelForm):
	class Meta: #permite utilizar los fields de Contacto
		model = Contacto
		fields = ["nombres","apellidos","cedula","email"] 