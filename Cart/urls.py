from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="cart"

urlpatterns = [
		path("add/<int:Item_id>/", views.AddingItem, name="add"),
		path("remove/<int:Item_id>/", views.RemovingItem, name="remove"),
		path("clear/", views.ClearCart, name="clear"),

]
