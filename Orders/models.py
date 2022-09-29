from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from Shop.models import Item
from django.db.models import F, Sum, FloatField

# Create your models here
User=get_user_model()

class Order(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)

	def __int__(self):
		return self.id

	@property
	def total(self):
		return self.orderline_set.aggregate(
			total=Sum(F("price")*F("units"), output_field=FloatField())
		)["total"]

	class Meta:
		db_table='orders'
		verbose_name='order'
		verbose_name_plural='orders'
		ordering=['id']

class orderline(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	item=models.ForeignKey(Item, on_delete=models.CASCADE)
	order=models.ForeignKey(Order, on_delete=models.CASCADE)
	units=models.IntegerField(default=1)
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.units} units || {self.item.name}'

	class Meta:
		db_table='orderslines'
		verbose_name='orderline'
		verbose_name_plural='orderlines'
		ordering=['id']

