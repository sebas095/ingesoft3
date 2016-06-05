from django import forms
from app.models import *

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		exclude = ['usuario','foto','activo']

class InmuebleForm(forms.ModelForm):
	class Meta:
		model = Inmueble
		exclude = ['usuario','activo']

class UploadFileForm(forms.Form):	# usado para subir imagen de perfil
    foto = forms.FileField()

