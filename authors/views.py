from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegisterForm # importando meu forms
from django.contrib import  messages # importando messages para o usuario


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)

    return render(
        request, 
        'authors/pages/register_view.html',
        {
            'form': form,
        },
    )

def register_create(request):
    if not request.POST:
        raise Http404

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    # validando um formulario no django
    if form.is_valid():
        # salvando dados na base de dados
        form.save()
        # messages para usuario
        messages.success(request,'Your user is create, pleace log in.')
        # deletando a chave de um dicionario - para limpar os dados de um formulario
        del(request.session['register_form_data'] )

    return redirect('authors:register')
