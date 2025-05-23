from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewsHome.as_view(), name="home"),
    path('recipes/search/', views.RecipeListViewsSearch.as_view(), name="search"),
    path('recipes/category/<int:category_id>/',
         views.RecipeListViewsCategory.as_view(), name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
