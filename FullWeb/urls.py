from django.urls import path
from FullWeb.views import home
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
		path('', home, name="home"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #CON ESTO LE DIGO A DJANGO DONDE DEBE CONSULTAR LOS ARCHIVOS DE MEDIA A TRAVEZ DE LA URL UBICADA EN  SETTINGS