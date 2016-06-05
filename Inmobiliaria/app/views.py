# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#importar modelos en caso de necestiar
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from app.forms import *
from app.models import *
from django.contrib.auth.models import User
#from django.core.mail import send_mail
import smtplib


@login_required
def inicio(request):	#pagina de inicio para usuarios
	#if request.user.is_staff:
	return render_to_response('usuarios/principal.html', context_instance=RequestContext(request))#[template_directory]/pregrep/index.html

@login_required
def addPub(request):
	usuario= get_object_or_404(User, id=request.user.id)
	if request.method == 'POST':
		form = InmuebleForm(request.POST)
		formfoto = UploadFileForm(request.POST, request.FILES)
		response_data = {}
		if form.is_valid():					# guardo datos
			informacion = form.save(commit=False)
			informacion.usuario = usuario
			informacion.save()


			informacion.foto1= request.FILES['foto1']
			informacion.foto2= request.FILES['foto2']
			informacion.foto3= request.FILES['foto3']
			informacion.foto4= request.FILES['foto4']


			informacion.save()


			response_data['message'] = 1	# Datos guardados satisfactoriamente
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			print form.errors
			response_data['message'] = form.errors		# formulario invalido, envio el error
			return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		return render_to_response('usuarios/crearPublicacion2.html',{'usuario':usuario}, context_instance=RequestContext(request))




@login_required
def listPub(request):
	usuario= get_object_or_404(User, id=request.user.id)
	publicaciones = Inmueble.objects.all()
	return render_to_response('usuarios/listarPublicacion.html',{'publicaciones':publicaciones,'usuario':usuario}, context_instance=RequestContext(request))

@login_required
def verPub(request,idPub):
	usuario = get_object_or_404(User, id=request.user.id)
	publicacion= get_object_or_404(Inmueble, id=idPub)
	return render_to_response('usuarios/verPublicacion.html',{'usuario':usuario, 'publicacion':publicacion},context_instance=RequestContext(request))
		