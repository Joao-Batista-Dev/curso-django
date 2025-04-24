from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegisterForm # importando meu forms
from django.contrib import  messages # importando messages para o usuario
from django.urls import reverse

def register_view(request):
    register_form_data = request.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)

    return render(
        request, 
        'authors/pages/register_view.html',
        {
            'form': form,
            'form_action': reverse('authors:register_create'),
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
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        # messages para usuario
        messages.success(request,'Your user is create, pleace log in.')
        # deletando a chave de um dicionario - para limpar os dados de um formulario
        del(request.session['register_form_data'] )

    return redirect('authors:register')


def login_views(request):
    return render(
        request,
        'authors/pages/login.html',
    )

def login_create(request):
    return render(
        request,
        'authors/pages/login.html',
    )