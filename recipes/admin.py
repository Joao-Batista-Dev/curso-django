from django.contrib import admin
from .models import Category, Recipe # Importando nosso models

# Registrando o nosso usuario
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Recipe) # Segunda - Forma de registrar Models 
class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin) # Primeira - Forma de registrar Models
