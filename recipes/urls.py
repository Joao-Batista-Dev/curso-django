from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewsHome.as_view(), name="home"),
    path('recipes/search/', views.RecipeListViewsSearch.as_view(), name="search"),
    path('recipes/tag/<slug:slug>/', views.RecipeListViewsTag.as_view(), name="tag"),
    path('recipes/category/<int:category_id>/', views.RecipeListViewsCategory.as_view(), name="category"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"),
    path('recipes/api/v1/', views.RecipeListViewsHomeApi.as_view(), name="recipe_api_v1"),
    path('recipes/api/v1/<int:pk>/', views.RecipeDetailApi.as_view(), name="recipe_api_v1_datail"),
    path('recipes/theory/', views.theory, name="theory"),
] + debug_toolbar_urls()

