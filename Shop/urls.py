from django.urls import path
from Shop.views import Shop
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
		path('shop/', Shop, name="shop"),
]
