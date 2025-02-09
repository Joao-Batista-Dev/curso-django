from django.shortcuts import render, get_list_or_404 # Importando o render - get_list_or_404 para error 
from django.http import HttpResponse # importando o Protocolo HTTP
from utils.recipes.factory import make_recipe # Importando pacote de dados FAKER
from .models import Recipe # Importando o models RECIPEencontrar retorna o error 404


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
    # Pegando dados e retornando error 404 se pagina não for encontrada
    recipes = get_list_or_404(
        Recipe.objects.filter(
        category__id=category_id,
        is_published = True, 
        ).order_by('-id',), 
    )

    return render(
        request, 
        'recipes/pages/home.html', # renderizar arquivo HTML
        context={ # passando um contexto para exibir no html = dicionario
            'recipes': recipes, # Para ixibir os dados para o usuário
            'title': f'{recipes[0].category.name} - Category' # Filtrando url pelo name
        }
    )

def recipe(request, id): # Criando minha views dinâmica
    recipe = Recipe.objects.filter(
        pk=id,
        is_published = True,
    ).order_by('-id').first()

    return render(
        request, 
        'recipes/pages/recipe-views.html', # renderizar arquivo HTML
        context={ # passando um contexto para exibir no html = dicionario
            'recipe': recipe, # chamando os dados da minha aplicacao
            'is_detail_page': True, # Ocuntando minha lista de detalhes
        }
    )