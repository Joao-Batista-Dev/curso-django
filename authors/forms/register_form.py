#from django.forms import Form, ModelForm
from django import forms # import forms
from django.contrib.auth.models import User # import models Users
from django.core.exceptions import ValidationError # import ValidationError
import re # importando minha regex
from utils.django_forms import strong_password # importando validacao - Regex

# criando forms atrelado ao models existente
class RegisterForm(forms.ModelForm):
    # outra forma de sobreescrever campos do formu
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex:. John'
        }),
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex:. Doe'
        }),
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username'
        }),
    )

    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your e-mail'
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password'
        }),
        # usando o meu validador de senha com regex
        validators=[strong_password]
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        }),
    )

    # criamos uma meta classe
    # paar passamos meta dados
    class Meta:
        # models que vamos usar
        model = User 
        # campos do formulario que queremos
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ] 

    # para validar um determinado campo - clean_nome-campo
    def clean_password(self):
        # cleaned_data - pegar o dados do formulario ja tratados - já data pegar crue
        data = self.cleaned_data.get('password')

        # verificao pra verificar determinado dado digitado em campo
        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(value)s no campo password',
                code='invalid',
                params={'value': '"atenção"'}
            )

        return data
    
    # clean - para que tenhamos apenas um email - email unico
    def clean_email(self):
        email = self.cleaned_data.get('email', '') # pegando dados do campo do meu email - do formulario
        exists = User.objects.filter(email=email).exists() # filtrar email na minha base de dados

        # vericar se esta cadastratando um email, ja cadastrado
        if exists:
            raise ValidationError(
                'User e-mail is already in use', 
                code='invalid',
            )

        return email


    # clean - para validar 2 campos do formulario com o mesmo dados
    def clean(self):
        # usando a super class com o metodo clean
        cleaned_data = super().clean()
        # pegando os dados do formulario
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        # fazendo verificao de error do formulario
        if password != password2:
            # levantando error do formulario
		    # levantando error e um dicionario para aparecer nos 2 campos
            raise ValidationError({
                # expecificando o campo do error - mais seu resultando sera exibido
                'password': 'password and password2 must be equal!',
                'password2': 'password and password2 must be equal!'
            })




