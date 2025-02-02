from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100) # Campo de Texto

# Criando minha Tabela para o meu Banco de Dados
class Recipe(models.Model):
    title = models.CharField(max_length=100) # Campo de Texto
    description = models.CharField(max_length=200) # Campo de Texto
    slug = models.SlugField() # Campo pra buscar
    preparation_time = models.IntegerField() # Campo para Numero
    preparation_time_unit = models.CharField(max_length=100) # Campo de Texto
    servings = models.IntegerField() # Campo para Numero
    servings_unit = models.CharField(max_length=200) # Campo de Texto
    preparation_steps = models.TextField() # Campo de Texto em formato maior
    preparation_steps_is_html = models.BooleanField(default=False) # Campo de Escolha que um boolean
    created_ad = models.DateTimeField(auto_now_add=True) # Campo de data = auto_now_add=True pegar a data que foi criada no dia e não alterar
    update_at = models.DateTimeField(auto_now=True) # Campo de data = auto_now=True pegar a data que foi criada
    is_published = models.BooleanField(default=False) # Campo de Escolha que um boolean
    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d/') # campo para pegar Imagem

    # Criando relacao com outra tabela
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)