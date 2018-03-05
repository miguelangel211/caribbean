"""caribbean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout_then_login
from home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index_view'),
    path('ruta/<int:id_ruta>',rutas,name='ruta'),
    path('agregarbasico/<id_boleto>/<id_ruta>',add_cart_boletobasico,name='agregarbasico'),
    path('agregaroro/<id_boleto>/<id_ruta>',add_cart_boletooro,name='agregaroro'),
    path('agregarvip/<id_boleto>/<id_ruta>',add_cart_boletovip,name='agregarvip'),
    path('agregarticketa/<id_boleto>/<id_ruta>',add_cart_ticketa,name='agregarticketa'),
    path('agregarticketr/<id_boleto>/<id_ruta>',add_cart_ticketr,name='agregar'),
    path('limpiar/',limpiar_cart,name='limpiar'),
    path('cart',cart,name='cart'),
    path('confirmacion',compraa,name="confirmacion"),
    path('login',login, {'template_name' : 'home/login.html'}, name='login'),
    path('logout',logout_then_login, name='logout_view'),
    path('administrador',administrador, name='administrador'),
    path('borrar',borrar,name='borrar'),
    path('baja',baja,name='baja'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG is True:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
