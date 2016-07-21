from django.contrib import admin
from .models import Contacto
from .models import Info
# Register your models here.

class AdministrarContacto(admin.ModelAdmin):
	list_display = ["__str__","nombres","apellidos","cedula","email"]
	list_editable = ["nombres","apellidos"]
	list_filter = ["email","cedula"]
	search_fields =["cedula","nombres"]
	class Meta:
		model = Contacto
admin.site.register(Contacto,AdministrarContacto)

#class AdministrarInfo(admin.ModelAdmin):
#	list_display = ["__str__","direccion","telefono"]
#	class Meta:
#		model = Info
#admin.site.register(Info,AdministrarInfo)