from django.shortcuts import render # Importando o render - renderizar o nossos arquivos HTML
from django.http import HttpResponse # importando o Protocolo HTTP

def home(request):
    return render(
        request, 
        'recipes/pages/home.html', # renderizar arquivo HTML
        context={ # passando um contexto para exibir no html = dicionario
            'name': 'João Batista'
        }
    )