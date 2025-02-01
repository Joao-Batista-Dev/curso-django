from django.shortcuts import render # Importando o render - renderizar o nossos arquivos HTML
from django.http import HttpResponse # importando o Protocolo HTTP
from utils.recipes.factory import make_recipe # Importando pacote de dados FAKER

def home(request):
    return render(
        request, 
        'recipes/pages/home.html', # renderizar arquivo HTML
        context={ # passando um contexto para exibir no html = dicionario
            'recipes': [make_recipe() for _ in range(10)], # chamando os dados da minha aplicacao
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