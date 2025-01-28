from django.urls import path
# Da pasta que estou importe views.py
from . import views 

urlpatterns = [
    path('', views.home), # importando minha rota views 
    path('recipes/<int:id>/', views.recipe), # criando minha url dinamica
]