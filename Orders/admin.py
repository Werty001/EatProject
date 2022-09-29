from django.contrib import admin
from Orders.models import Order, orderline

admin.site.register(Order)
admin.site.register(orderline)