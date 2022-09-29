from pyexpat import model
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name=models.CharField(max_length=30,null=True)
	created=models.DateField(auto_now_add=True)
	uploaded=models.DateField(auto_now_add=True)
	class Meta:
		verbose_name='category'
		verbose_name_plural='categories'
	def __str__(self):
		return self.name

class Item (models.Model):
	name=models.CharField(max_length=30,null=True)
	description=models.CharField(max_length=50)
	price=models.FloatField()
	image=models.ImageField(upload_to='blog',null=True, blank=True)
	owner=models.ForeignKey(User, on_delete=models.CASCADE)
	categories=models.ManyToManyField(Category)
	created=models.DateField(auto_now_add=True)
	uploaded=models.DateField(auto_now_add=True)
	class Meta:
		verbose_name='item'
		verbose_name_plural='items'
	def __str__(self):
		return self.name