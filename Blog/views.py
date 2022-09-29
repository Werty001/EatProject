from django.shortcuts import render
from Blog.models import Category, Post

def blog(request):
	Postlist=Post.objects.all()
	return render(request, 'Blog/blog',{'posts': Postlist})  

def categorie(request, categorie_id):
	categorieid=Category.objects.get(id=categorie_id)
	categorielist=Post.objects.filter(categories=categorieid)
	return render(request, 'Blog/categorie',{'categorie': categorieid,'posts': categorielist})  