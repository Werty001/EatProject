from cmath import log
from django.urls import path
from.views import Log_in, RegisterView, Log_out
urlpatterns = [
		path('register/', RegisterView.as_view(), name="register"),
		path('logout/', Log_out, name="logout"),
		path('login/', Log_in, name="login"),
]

 