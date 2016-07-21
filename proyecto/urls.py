"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#importa las vistas 
from servicioWeb.views import ClienteViewSet, CajaAhorrosViewSet, CuentaAhorrosViewSet
from rest_framework.routers import DefaultRouter

#definir las clases commo una ruta normal
router = DefaultRouter()
router.register(r'cliente',ClienteViewSet)
router.register(r'caja',CajaAhorrosViewSet)
router.register(r'cuenta',CuentaAhorrosViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^caja/', include('caja.urls')),
    #url(r'^$','caja.views.nuevo_user',name='nuevo_user'),   
    url(r'^$','agenda.views.inicio',name='inicio'),
    url(r'^api/', include(router.urls)),
]
    