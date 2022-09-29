from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Orders.models import Order, orderline
from Cart.cart import Cart
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

#@login_required(login_url="authentication/Login")
def orders(request):
	order=Order.objects.create(user=request.user)
	cart=Cart(request)
	order_lines=list()
	for key, value in cart.cart.items():
		order_lines.append(orderline(
			item_id=key,
			units=value["unit"],
			user=request.user, 
			order=order
		))
	orderline.objects.bulk_create(order_lines)

	send_ordermail(
		order=order,
		order_lines=order_lines,
		username=request.user.username,
		useremail=request.user.email,
		)
	#cart.cleanCart()
	return render (request, "OrderSuccess")

def send_ordermail(**kwargs):
	subjet=("Order N*:  from GESTION PEDIDOS")
	message=render_to_string("email/order.html",{
		"order": kwargs.get("order"),
		"order_lines": kwargs.get("order_lines"),
		"username": kwargs.get("username"),
	})
	message_text=strip_tags(message)
	from_email="ruggero.an@gmail.com"
	#to_email=kwargs.get("useremail")
	to_email="an_ruggero@hotmail.com"
	send_mail(subjet,message_text,from_email,[to_email],html_message=message)
