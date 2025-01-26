from django.urls import path
from . views import home # Importando minhas views.py do meu app

# dominio/recipes/contato
urlpatterns = [
    path('', home), # rota home
]