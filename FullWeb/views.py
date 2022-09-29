import re
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse
from Cart.views import Cart


# Create your views here.


def home(request):
	cart=Cart(request)
	return render(request, "FullWeb/home.html") 

def shop(request):
	return render(request, 'FullWeb/shop') 

def contact(request):
	return render(request, 'FullWeb/contact') 
	