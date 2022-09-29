from django.urls import path
from Contact.views import Contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
		path('contact/', Contact, name="contact"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #CON ESTO LE DIGO A DJANGO DONDE DEBE CONSULTAR LOS ARCHIVOS DE MEDIA A TRAVEZ DE LA URL UBICADA EN  SETTINGS 