from django.contrib import admin
from django.urls import path, include # importando o include
from django.conf.urls.static import static # Importando arquivos staticos
from django.conf import settings # Importando arquivos do arquivos settings
 

urlpatterns = [
    path('admin/', admin.site.urls), # rota django admin
    path('', include('recipes.urls')), # include('meu-app.urls.py')
    path('authors/', include('authors.urls')), # incluindo meu segundo app
]

# configurando urls das nossas imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

