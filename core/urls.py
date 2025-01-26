from django.contrib import admin
from django.urls import path, include # impotando o include

urlpatterns = [
    path('admin/', admin.site.urls), # rota django admin
    path('', include('recipes.urls')), # include('meu-app.urls.py')
    # path('recipes/', include('recipes.urls')) # urls dentro de um subdominio
]
