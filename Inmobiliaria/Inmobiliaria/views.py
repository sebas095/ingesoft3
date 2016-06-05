from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def index_page(request):
	return render_to_response('usuarios/index.html',context_instance=RequestContext(request))


def login_page(request):
	if not request.user.is_anonymous():	
		return redirect('inicio')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username = username, password = clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return redirect('inicio')
				else:
					return redirect('login')
			else:
				return render_to_response('usuarios/login.html',{'message':'no eres usuario'},context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()

	return render_to_response('usuarios/login.html',{'formulario':formulario},context_instance=RequestContext(request))

def logout_page(request):
	logout(request)
	print request
	return redirect('login')