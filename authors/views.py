from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegisterForm, LoginForm
'''
importando messages para o usuario
'''
from django.contrib import  messages 
from django.urls import reverse
'''
para fazer autheticacao do meu formulario
login para logar - usuario logado no sistema
'''
from django.contrib.auth import authenticate, login, logout 
'''
Decorator que colocamos na views para ela ser restrita
'''
from django.contrib.auth.decorators import login_required 

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

    '''
    validando um formulario no django
    '''
    if form.is_valid():
        '''
        salvando dados na base de dados
        '''
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        
        '''
        messages para usuario
        '''
        messages.success(request,'Your user is create, pleace log in.')
        
        '''
        deletando a chave de um dicionario - para limpar os dados de um formulario
        '''
        del(request.session['register_form_data'] )
        
        return redirect(reverse('authors:login'))

    return redirect('authors:register')


def login_views(request):
    form = LoginForm()

    return render(
        request,
        'authors/pages/login.html',
        {
        'form': form,
        'form_action': reverse('authors:login_create')
        }
    )

def login_create(request):
    if not request.POST:
        raise Http404
    
    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        '''
        pegar dados do campo form: usuario e senha
        '''
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''), 
        )
        '''
        veficar se os dado e autenciado
        '''
        if authenticated_user is not None:
            messages.success(
                request,
                'Your are logged in.'
            )

            '''
            para fazer login do usuario
            '''
            login(request, authenticated_user) 

            return redirect(login_url)
        else:
            messages.error(
                request,
                'Invalid credentials'
            )

            return redirect(login_url)
    else:
        messages.error(
            request,
            'Invalid username or password'
        )

    return redirect(login_url)

'''
logout - usuario logado no sistema
decorator - para views ser fechada - precisa que usuario esteja,
logado pra acesssa determinada pagina
'''
@login_required(login_url='authors:login', redirect_field_name='next')
def logout_views(request):
    if not request.POST:
        return redirect(reverse('authors:login'))
    
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authors:login'))

    logout(request)

    return redirect(reverse('authors:login'))