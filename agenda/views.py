from django.shortcuts import render
from .models import Contacto,Info
from .forms import Formulario
from .forms import FormularioModeloA


# Create your views here.

def inicio(request):
	f = FormularioModeloA(request.POST or None)
	context = {
		"Titulo":"Formulario de registro de Contacto",
		"form":f
	}
	if f.is_valid():
		datos_form = f.cleaned_data
		nom_form = datos_form.get("nombres")
		ape_form = datos_form.get("apellidos")
		ced_form = datos_form.get("cedula")
		corr_form = datos_form.get("email")
		obj = Contacto.objects.create(nombres=nom_form,apellidos=ape_form,cedula=ced_form,email=corr_form)
		if obj:
			context ={
				"Titulo":"Se guardo el nuevo Contacto"
			}

		#se crea internamente el summit luego de crear el objeto
		#summit --> True valida todos los campos y guarada en la base de datos
		#summit --> False valida los campos pero no modifica la bd solo crea el objeto

	return render(request,"inicio.html",context)#enviamos en context (cuerpo del formulario) donde estara escritos los datos del modelo

def caratula(request):
	return render(request,'caratula.html',{})

def presentacion(request):
	return render(request,'presentacion.html',{})