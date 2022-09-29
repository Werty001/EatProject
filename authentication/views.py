from collections import UserList
from distutils.log import error
from multiprocessing.pool import IMapUnorderedIterator
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


class RegisterView(View):
	def get(self,request):
		form=UserCreationForm()
		return render(request,"Auth/Register",{"form":form})

	def post(self,request):
		form=UserCreationForm(request.POST)
		if form.is_valid():
			userinfo=form.save()
			login(request, userinfo)
			return redirect('home')
		else:
			for msg in form.error_messages:
				messages.error(request, form.error_messages[msg])
			return render(request,"Auth/Register",{"form":form})

def Log_out(request):
	logout(request)
	return redirect('home')

def Log_in(request):
	if request.method=="POST":
		form=AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			User_name=form.cleaned_data.get("username")
			Password=form.cleaned_data.get("password")
			User=authenticate(username=User_name,password=Password)
			if User is not None:
				login(request, User)
				return redirect('home')
			else:
				messages.error(request, "This user does not exist")
		else:
			messages.error(request, "Invalid information")
	form=AuthenticationForm()
	return render(request,"Auth/Login",{"form":form})
 