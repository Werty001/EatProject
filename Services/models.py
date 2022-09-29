import datetime
from distutils.command import upload
from tabnanny import verbose
from django.db import models
from django.forms import DateField, ImageField
from psycopg2 import Date
from traitlets import default

# Create your models here.
class Service(models.Model):
	title=models.CharField(max_length=30,null=True)
	contenido=models.CharField(max_length=50)
	image=models.ImageField(upload_to='services',null=True)
	created=models.DateField(auto_now_add=True)
	uploaded=models.DateField(auto_now_add=True)
	class Meta:
		verbose_name='service'
		verbose_name_plural='services'
	def __str__(self):
		return self.title