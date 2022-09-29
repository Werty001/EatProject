from django.urls import path
from Blog.views import blog, categorie
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
		path('blog/', blog, name="blog"),
		path('blog/categorie/<int:categorie_id>/', categorie, name="categorie"), 
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #CON ESTO LE DIGO A DJANGO DONDE DEBE CONSULTAR LOS ARCHIVOS DE MEDIA A TRAVEZ DE LA URL UBICADA EN  SETTINGS