from django.urls import path
from Services.views import services
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
		path('services/', services, name="services"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #CON ESTO LE DIGO A DJANGO DONDE DEBE CONSULTAR LOS ARCHIVOS DE MEDIA A TRAVEZ DE LA URL UBICADA EN  SETTINGS