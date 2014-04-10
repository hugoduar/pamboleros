from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from models import Publicacion
# Create your views here.

def index(request):
	context = RequestContext(request)
	if request.user.is_active:
		return HttpResponseRedirect('/noticias')
	else:
		return render_to_response('index.html', {}, context)

@login_required(login_url='/')
def noticias(request):
	context = RequestContext(request)
	publicaciones = Publicacion.objects.all()
	return render_to_response('noticias.html', {'publicaciones': publicaciones}, context)

def login(request):
	context = RequestContext(request)
	exists = True
	if request.method == 'POST':
		username = request.POST['usuario']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				exists = True
				paso = 'paso: ' + request.user.username
			else:
				pass	
		else: 
			pass
	else:
		pass
	return noticias(request)

def logout(request):
	context = RequestContext(request)
	auth_logout(request)
	return HttpResponseRedirect('/')
