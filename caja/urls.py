from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [     
	url(r'^$','caja.views.listar'),
	url(r'^crear/$','caja.views.crear'),
	url(r'^modificar/$','caja.views.modificar'),
	url(r'^eliminar/$','caja.views.eliminar'),     
	url(r'^eliminarCliente/$','caja.views.eliminarCliente'),    
	url(r'^cuentas/$','caja.views.cuentas'),
	url(r'^cuentas/crearcuenta/$','caja.views.crearcuenta'),
	url(r'^transaccion$','caja.views.transaccion'),
	url(r'^eliminarcuenta/$','caja.views.eliminarcuenta'),
	url(r'^cuentas/activarcuenta/$','caja.views.activarcuenta'),     
	url(r'^nuevo_user/$','caja.views.nuevo_user'),
	url(r'^reporte/$','caja.views.reporte'),
	url(r'^pdf/$','caja.views.pdf'),
	url(r'^confirmacion_eliminar_cu/$','caja.views.confirmacion_eliminar_cu'),
	url(r'^ver_listado/$','caja.views.ver_listado'),
	]
