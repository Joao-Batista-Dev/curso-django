from django.urls import path
# Da pasta que estou importe views.py
from . import views 

# reipes:home
app_name = "recipes"

urlpatterns = [
    path('', views.home, name="home"), # importando minha rota views 
    path('recipes/<int:id>/', views.recipe, name="recipe"), # criando minha url dinamica
]