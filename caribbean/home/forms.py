from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Usuario_form(forms.ModelForm):
	CATH_CHOICES=(
			('Gerencia','Gerencia'),
			('Cajero','Cajero'),
			('Repartidor','Repartidor'),
			)
	username=forms.CharField(label='Usuario')
	email=forms.EmailField(label='Correo')
	email2=forms.EmailField(label='comfirmar correo')
	password=forms.CharField(label='contrasena',widget=forms.PasswordInput)
	password2=forms.CharField(label='confirmar contrasena',widget=forms.PasswordInput)
	first_name=forms.CharField(label='Nombre')
	last_name=forms.CharField(label='Apellidos')
	def __init__(self,*args,**kwargs):
		super(Usuario_form,self).__init__(*args,**kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class':'form-control'
				})
	class Meta:
		model = User
		fields = [
		'username',
		'email','email2',
		'password','password2',
		'first_name',
		'last_name',
		]
	def clean(self):
		email=self.cleaned_data.get('email')
		email2=self.cleaned_data.get('email2')
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		password2=self.cleaned_data.get('password2')
		if email != email2:
			raise forms.ValidationError("Los correos no coinciden")
		if password != password2:
			raise forms.ValidationError("Las contrasenas no coinciden")
		return self.cleaned_data



class NameForm(forms.ModelForm):
    class Meta:
        model = compra
        fields = [
        'Nombre',
        'rfc','email',
        ]

class subscriptoresForm(forms.ModelForm):
    class Meta:
        model = subscriptores
        fields = [
			'email','Nombre'
        ]
