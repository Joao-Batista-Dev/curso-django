from django.shortcuts import render # Importando o render - renderizar o nossos arquivos HTML
from django.http import HttpResponse # importando o Protocolo HTTP
from utils.recipes.factory import make_recipe # Importando pacote de dados FAKER
from recipes.models import Recipe # Importando o models RECIPE

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True, # Aplicando filtro na minhas publicacao
        ).order_by(
            '-id',
            ) # Pegando os dados do nosso models e ordenando em ordem descrecente
    
    return render(
        request, 
        'recipes/pages/home.html', # renderizar arquivo HTML
        context={ # passando um contexto para exibir no html = dicionario
            'recipes': recipes, # Para ixibir os dados para o usuário
        }
    )

# Criando a views de categoria
def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published = True,  # Aplicando filtro na minhas publicacao
        ).order_by(
            '-id',
            ) # Pegando os dados do nosso models e ordenando em ordem descrecente
    
    return render(
        request, 
        'recipes/pages/home.html', # renderizar arquivo HTML
        context={ # passando um contexto para exibir no html = dicionario
            'recipes': recipes, # Para ixibir os dados para o usuário
        }
    )

def recipe(request, id): # Criando minha views dinâmica
    return render(
        request, 
        'recipes/pages/recipe-views.html', # renderizar arquivo HTML
        context={ # passando um contexto para exibir no html = dicionario
            'recipe': make_recipe(), # chamando os dados da minha aplicacao
            'is_detail_page': True, # Ocuntando minha lista de detalhes
        }
    )