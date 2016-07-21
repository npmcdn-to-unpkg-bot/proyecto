from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
#encoding:utf-8
from reportlab.pdfgen import canvas
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime

from .forms import Formulario, Formulario_Crear, Formulario_Modificar
from .forms import Formulario_Eliminar, Formulario_Cliente_M, Formulario_usuario, Formulario_Transaccion
from .models import Cliente, CajaAhorros, CuentaAhorros, Transaccion
# Create your views here.

def nuevo_user(request):
	f = Formulario_usuario(request.POST or None)
	context = {
		'form':f,
	}
	mensaje=''
	if request.method=="POST":
		username = request.POST["username"]
		password = request.POST["password"]
		usuario = authenticate(username=username, password=password)
		if usuario is not None:
			if usuario.is_active:
				login(request,usuario)
				messages.add_message(request, messages.SUCCESS, "Usuario Valido", fail_silently=True)
				return redirect(listar)
			else:
				messages.add_message(request, messages.ERROR, "Contrasenia Invalida", fail_silently=True)
		else:
			messages.add_message(request, messages.ERROR, "Usuario y Contrasenia Invalidos", fail_silently=True)
			return redirect(nuevo_user)
		context = {
			'mensaje':mensaje,
		}
	return render(request,'nuevo_user.html',context)
	
	#if user is not None:
	#if request.method=='POST'
	#return redirect('nuevo_user')
#	else:
	
@login_required(login_url='nuevo_user')
def listar(request):
	f = Formulario(request.POST or None)
	clientes = Cliente.objects.all()
	context = {
		"form":f,
		'clientes':clientes,
	}
	return render(request,'listar.html',context)

def crear(request):
	f = Formulario_Crear(request.POST or None)
	context ={
		"Titulo1":"Formulario para crear datos",
		"form":f,
	}

	if f.is_valid():
		datos_form = f.cleaned_data
		cliente = Cliente()
		cliente.idCA = CajaAhorros.objects.all()[0]
		cliente.nombres = datos_form.get("nombres")
		cliente.apellidos = datos_form.get("apellidos")
		cliente.cedula = datos_form.get("cedula")
		cliente.correo = datos_form.get("correo")
		cliente.telefono = datos_form.get("telefono")
		cliente.celular = datos_form.get("celular")
		cliente.direccion = datos_form.get("direccion")
		cliente.genero = datos_form.get("genero")
		cliente.estadoCivil = datos_form.get("estadoCivil")
		cliente.fechaNacimiento = datos_form.get("fechaNacimiento")
		
		if (cliente.save() != True):
			cuenta=CuentaAhorros()
			cuenta.cliente=cliente
			cuenta.numeroCuenta = len(CuentaAhorros.objects.all())+1
			cuenta.estado = True
			cuenta.saldo = 0
			cuenta.save()
			if (cuenta.save()):
				context={
					'validar':"Se creo correctamente su cuenta",
				}
			
			return redirect('/caja')
	context ={
		"form":f,
	}
	return render(request,'crear.html',context)

def buscar(request):
	return render(request,'buscar.html',{})

def modificar(request):
	cliente = Cliente.objects.get(cedula=request.GET['cedula'])
	#f = Formulario_Modificar(request.POST or None)
	f = Formulario_Cliente_M(request.POST or None)
	context={
		'cliente':cliente,
		'form':f,
   	} 
	
	f.fields["nombres"].initial = cliente.nombres
	f.fields["apellidos"].initial = cliente.apellidos
	#f.fields["cedula"].initial = cliente.cedula
	f.fields["correo"].initial = cliente.correo
	f.fields["telefono"].initial = cliente.telefono
	f.fields["celular"].initial = cliente.celular
	f.fields["direccion"].initial = cliente.direccion
	f.fields["genero"].initial = cliente.genero
	f.fields["estadoCivil"].initial = cliente.estadoCivil
	f.fields["fechaNacimiento"].initial = cliente.fechaNacimiento

	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			cliente.nombres = f_data.get("nombres")
			cliente.apellidos = f_data.get("apellidos")
			cliente.correo  = f_data.get("correo")
			cliente.telefono = f_data.get("telefono")
			cliente.celular = f_data.get("celular")
			cliente.direccion = f_data.get("direccion")
			cliente.genero = f_data.get("genero")
			cliente.estadoCivil = f_data.get("estadoCivil")
			cliente.fechaNacimiento = f_data.get("fechaNacimiento")
			if (cliente.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el cliente", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el cliente", fail_silently=True)
			return redirect(listar)

	return render(request,'modificar.html',context)

def eliminar(request):
	cliente = Cliente.objects.get(cedula=request.GET['cedula'])
	context = {
		'cliente':cliente,
	}
	return render(request,'eliminar.html',context)

def eliminarCliente(request):
	cliente = Cliente.objects.get(cedula=request.GET['cedula'])
	if (cliente.delete()):
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el cliente", fail_silently=True)
	else: 
		messages.add_message(request, messages.ERROR, "No se ha eliminado el cliente", fail_silently=True)
	return redirect(listar)

def cuentas(request):
	cl = Cliente.objects.get(cedula=request.GET['cedula'])
	listacuentas = CuentaAhorros.objects.filter(cliente=cl)
	context={
		'cliente':cl,
		'listacuentas':listacuentas,
	}
	return render(request,'cuentas.html',context)

def activarcuenta(request):
	ced=request.GET['cedula'] 
	cuenta=request.GET['cuenta']
	cu= CuentaAhorros.objects.get(numeroCuenta=cuenta)
	if(cu.estado==True):
		cu.estado=False
	else:
		cu.estado=True
	cu.save()
	return redirect("/caja/cuentas?cedula="+ced)

def crearcuenta(request):
	ced=request.GET['cedula'] #recibe la cedula que envio
	cl = Cliente.objects.get(cedula=ced) #la cedula que envio con la que recibo deben ser =
	objcuenta = CuentaAhorros() #objeto de la cuenta ahorros
	objcuenta.cliente=cl #referencia de la cuenta ahorros igual al id del cliente
	objcuenta.numeroCuenta = len(CuentaAhorros.objects.all())+1 
	objcuenta.estado = True
	objcuenta.saldo = 10.00
	objcuenta.save()

	return redirect('/caja/cuentas?cedula='+ced)
	#return render(request,'cuentas.html',{})

def eliminarcuenta(request):
	ced=request.GET['cedula']
	cuenta = request.GET['cuenta']
	cu=CuentaAhorros.objects.get(numeroCuenta=cuenta)
	cu.delete()
	return redirect('/caja/cuentas?cedula='+ced)
	#return render(request,'eliminarcuenta.html',{})

def transaccion(request):
	f = Formulario_Transaccion(request.POST or None)
	mensaje=''
	if request.method=="POST":
		if f.is_valid():
			datos = f.cleaned_data
			cuenta = CuentaAhorros.objects.get(numeroCuenta=request.GET['numeroCuenta'])
			t=Transaccion()
			t.idCuenta=cuenta
			t.tipo=datos.get("tipo")
			t.descripcion=datos.get("descripcion")
			t.valor=datos.get("valor")
			t.fecha=datetime.now()
			if(t.tipo=="deposito"):
				cuenta.saldo=cuenta.saldo+t.valor
				mensaje="Deposito realizado con exito"
				cuenta.save()
				t.save()
				return redirect(listar)
			else:
				if(cuenta.saldo>t.valor):
					cuenta.saldo=cuenta.saldo-t.valor
					mensaje="Retiro realizado con exito"
					cuenta.save()
					t.save()
					return redirect(listar)
				else:
					mensaje="Saldo insuficiente para la transaccion"
	context ={
		"form":f,
		"mensaje":mensaje,
	}
	return	render(request,'transaccion.html',context)

def reporte(request):
	response =HttpResponse(content_type='application/pdf') 
	response['Content-Disposition'] = 'attachment; filename=documento.pdf' 
	ced=request.GET['cedula']
	cliente=Cliente.objects.get(cedula=ced) 
	p = canvas.Canvas(response) 
	p.drawString(300, 800, "DATOS CLIENTE") 
	p.drawString(20, 750, "Nombre:") 
	p.drawString(20, 730, "Apellido:") 
	p.drawString(20, 710, "Cedula:") 
	p.drawString(20, 690, "Correo:") 
	p.drawString(20, 670, "Telefono:") 
	p.drawString(20, 650, "Celular:") 
	p.drawString(20, 630, "Direccion:") 
	p.drawString(20, 610, "Sexo:") 
	p.drawString(20, 590, "Estado Civil:") 
	p.drawString(20, 570, "Fecha de Nacimiento:") 
	p.drawString(150, 750, cliente.nombres) 
	p.drawString(150, 730, cliente.apellidos) 
	p.drawString(150, 710, cliente.cedula) 
	p.drawString(150, 690, cliente.correo) 
	p.drawString(150, 670, cliente.telefono) 
	p.drawString(150, 650, cliente.celular) 
	p.drawString(150, 630, cliente.direccion) 
	p.drawString(150, 610, cliente.genero) 
	p.drawString(150, 590, cliente.estadoCivil) 
	t=cliente.fechaNacimiento 
	p.drawString(150, 570,t.strftime('%m/%d/%Y')) 
	p.showPage() 
	p.save() 
	return response

def pdf(request):
	with open('C:\Users\Chris\Downloads\documento.pdf', 'r') as pdf:
		#pdf.encode('utf-8').strip()
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline;filename=reporte.pdf'
		return response
	pdf.closed

	
