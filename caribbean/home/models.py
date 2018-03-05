# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User,Group
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
# Create your models here.


class ruta(models.Model):
    Duracion=models.IntegerField(),
    Nombre = models.CharField(max_length=30)
    descriptcion=models.CharField(max_length=500)
    destinos=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='')
    def url(self):
        if self.imagen and hasattr(self.imagen,'url'):
            return self.imagen.url


class boleto(models.Model):
    ruta=models.ForeignKey(ruta,on_delete=models.CASCADE)
    precio=models.DecimalField(max_digits=9,decimal_places=2)
    descriptcion=models.CharField(max_length=300)

class boleto_basico(boleto):
    Nombreb=models.CharField(max_length=30,default="Boleto basico")

class boleto_oro(boleto):
    Nombreb=models.CharField(max_length=30,default="boleto oro")

class boleto_vip(boleto):
    NOmbreb= models.CharField(max_length=30, default="boleto vip")

class ticket_actividad(boleto):
    Nombreta=models.CharField(max_length=30)
    Dias=models.CharField(max_length=30)
    horarios=models.CharField(max_length=30)

class ticket_restaurante(boleto):
    Nombretr=models.CharField(max_length=30)
    restaurante=models.CharField(max_length=30)

class compra(models.Model):
    Nombre=models.CharField(max_length=40)
    rfc=models.CharField(max_length=15)
    email=models.EmailField()
    descripcion= models.CharField(max_length=500)
    subtotal=models.DecimalField(max_digits=12,decimal_places=2)
    iva=models.DecimalField(max_digits=12,decimal_places=2)
    total=models.DecimalField(max_digits=12,decimal_places=2)
    timestamp=models.DateTimeField(auto_now_add=True,null=True)

class subscriptores(models.Model):
    email=models.EmailField()
    Nombre=models.CharField(max_length=30)
