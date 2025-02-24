from django.shortcuts import render, get_list_or_404, get_object_or_404 # Importando o render - get_list_or_404 para error 
from django.http import HttpResponse, Http404 # importando o Protocolo HTTP
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
    recipe = get_object_or_404(
        Recipe,
        pk=id,
        is_published = True,
    )

    return render(
        request, 
        'recipes/pages/recipe-views.html', # renderizar arquivo HTML
        context={ # passando um contexto para exibir no html = dicionario
            'recipe': recipe, # chamando os dados da minha aplicacao
            'is_detail_page': True, # Ocuntando minha lista de detalhes
        }
    )

def search(request):
    search_term = request.GET.get('q')

    if not search_term:
        raise Http404()
    
    return render(request, 'recipes/pages/search.html')