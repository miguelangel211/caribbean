from django.shortcuts import render
import json
import decimal
import simplejson
# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group,User
from django.shortcuts import render,redirect
from django.views.generic import CreateView, FormView, ListView, DetailView,UpdateView,DeleteView
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from decimal import Decimal
from django.core.mail import send_mail
# Create your views here.

def index(request):
    p =ruta.objects.raw('SELECT * FROM home_ruta')
    return render(request,'home/index.html',{'categoria':p})

def rutas(request,id_ruta):
    rutas=ruta.objects.get(id=id_ruta)
    boleto_basicos=boleto_basico.objects.get(ruta=rutas)
    boleto_oros=boleto_oro.objects.get(ruta=rutas)
    boleto_vips=boleto_vip.objects.get(ruta=rutas)
    ticket_actividads=ticket_actividad.objects.filter(ruta=rutas)
    ticket_restaurantes=ticket_restaurante.objects.filter(ruta=rutas)
    datos={
    'ruta':rutas,
    'boleto_basico':boleto_basicos,
    'boleto_oro':boleto_oros,
    'boleto_vip':boleto_vips,
    'ticket_actividad':ticket_actividads,
    'ticket_restaurante':ticket_restaurantes,
    }
    return render(request,'home/ruta.html',{'datos':datos})

def add_cart_boletobasico(request,id_boleto,id_ruta):
    lista=request.session.get('carro',[])
    lista.append(simplejson.dumps(list(boleto_basico.objects.filter(id=id_boleto).values())))
    request.session['carro']=lista
    return redirect('ruta', id_ruta=id_ruta)

def add_cart_boletooro(request,id_boleto,id_ruta):
    lista=request.session.get('carro',[])
    lista.append(simplejson.dumps(list(boleto_oro.objects.filter(id=id_boleto).values())))
    request.session['carro']=lista
    return redirect('ruta', id_ruta=id_ruta)

def add_cart_boletovip(request,id_boleto,id_ruta):
    lista=request.session.get('carro',[])
    lista.append(simplejson.dumps(list(boleto_vip.objects.filter(id=id_boleto).values())))
    request.session['carro']=lista
    return redirect('ruta', id_ruta=id_ruta)

def add_cart_ticketa(request,id_boleto,id_ruta):
    lista=request.session.get('carro',[])
    lista.append(simplejson.dumps(list(ticket_actividad.objects.filter(id=id_boleto).values())))
    request.session['carro']=lista
    return redirect('ruta', id_ruta=id_ruta)

def add_cart_ticketr(request,id_boleto,id_ruta):
    lista=request.session.get('carro',[])
    lista.append(simplejson.dumps(list(ticket_restaurante.objects.filter(id=id_boleto).values())))
    request.session['carro']=lista
    return redirect('ruta', id_ruta=id_ruta)

def limpiar_cart(request):
    del request.session['carro']
    return redirect('/')


def administrador(request):
    totalcompleto=0
    if request.user.groups.filter(name="administrador"):
        subscriptor=subscriptores.objects.raw('SELECT * FROM home_subscriptores')
        compras=compra.objects.raw('SELECT * FROM home_compra')
        for n in compras:
            totalcompleto=totalcompleto+n.total
        return render(request,'home/administrador.html',{'subscriptores':subscriptor,'compras':compras,'total':totalcompleto})
    else:
        return redirect('/admin')


def cart(request):
    lista=[]
    subtotal=0
    iva=.16
    total=0
    for key in request.session.get('carro',[]):
        lista.append(simplejson.loads(key))
    for obj in lista:
        for o in obj:
                subtotal=subtotal+o['precio']
    iva=subtotal*iva
    total=subtotal+iva
    request.session['iva']=iva
    request.session['subtotal']=subtotal
    request.session['total']=total
    return render(request,'home/cart.html',{'cart':lista,'total':total,'subtotal':subtotal,'iva':iva})


def compraa(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.descripcion=request.session['carro']
            user.subtotal=request.session['subtotal']
            user.iva=request.session['iva']
            user.total=request.session['total']
            user.save()
            if 'suscribir' in request.POST:
                form2=subscriptoresForm(request.POST)
                if form2.is_valid():
                    form2.save()
                send_mail(
        'Confirmacion de subscripcion',
        'subscrito a caribbean tour',
        'from@example.com',
        [request.POST['email']],
        fail_silently=False,
    )
    del request.session['carro']
    del request.session['subtotal']
    del request.session['iva']
    del request.session['total']
    return render(request,'home/confirmacion.html')

def borrar(request):
    email=request.POST['email']
    subscriptores.objects.filter(email=email).delete()
    return redirect('/')

def baja(request):
    return render(request,'home/borrar.html')
