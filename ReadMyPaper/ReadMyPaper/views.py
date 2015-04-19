from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyUserCreationForm

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html' , c)

def auth_view(request):
	username = request.POST.get('username' , '')
	password = request.POST.get('password' , '')
	user = auth.authenticate(username = username , password = password)

	if user is not None:
		auth.login(request , user)
		return HttpResponseRedirect ('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html')

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid() and request.username.endswith("@trincoll.edu"):
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))
	args['form'] = MyUserCreationForm() 
	
	#May be for debugging
	print args

	return render_to_response('register.html' , args)

def register_success(request):
	return render_to_response('register_success.html')

def termsofuse(request):
	return render_to_response('termsofuse.html')
	
	
#method for getting the username
def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username