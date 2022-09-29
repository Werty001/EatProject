from django.shortcuts import render
from Services.models import Service


def services(request): 
	serviceslist=Service.objects.all()
	return render(request, 'Services/services',{'services': serviceslist})  

