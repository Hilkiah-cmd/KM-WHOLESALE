from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm

from .models import Product
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render(),{'products':products})

@csrf_exempt
def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(home)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})

def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("km:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())

def signout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("km:index")