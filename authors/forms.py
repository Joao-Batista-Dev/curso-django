#from django.forms import Form, ModelForm
from django import forms # import forms
from django.contrib.auth.models import User # import models Users

# criando forms atrelado ao models existente
class RegisterForm(forms.ModelForm):
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

        # sobrescrever um input - inserindo determinado dados
        widget = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha corretar'
            })  
        }
        
        # para excluir um campo do formulario
        # exclude = ['firts_name']

        # para escrevemos no campos do input
        # label = { 'username': 'Digite seu usuário' }

        # menssagem de ajudar para o usuário
        # help_texts = { 'email': 'Digite um Email válido!' }