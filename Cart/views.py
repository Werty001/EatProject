from re import I
from django.shortcuts import redirect
from .cart import Cart
from Shop.models import Item
# Create your views here.

def AddingItem(request, Item_id):
	cart=Cart(request)
	item=Item.objects.get(id=Item_id)
	cart.addItem(Item=item)
	return redirect("shop")

def RemovingItem(request, Item_id):
	cart=Cart(request)
	item=Item.objects.get(id=Item_id)
	cart.subtractItem(Item=item)
	return redirect("shop")

def ClearCart(request):
	cart=Cart(request)
	cart.cleanCart()
	return redirect("shop")
