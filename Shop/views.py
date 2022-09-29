from django.shortcuts import render
from .models import Item, Category
# Create your views here.

def Shop(request):
	Shoplist=Item.objects.all()
	return render(request, 'Shop/',{'items': Shoplist})

def categorie(request, categorie_id):
	categorieid=Category.objects.get(id=categorie_id)
	categorielist=Item.objects.filter(categories=categorieid)
	return render(request, 'Blog/categorie',{'categorie': categorieid,'posts': categorielist})