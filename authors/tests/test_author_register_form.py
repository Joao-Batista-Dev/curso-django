# Importa a classe base de teste do Django. 
# unittest - mais rapido
from unittest import TestCase
'''
Importa o formulário que será testado. 
Esse formulário está em authors/forms.py.
'''
from authors.forms import RegisterForm
'''
Importa o decorador @parameterized.expand que 
permite testar o mesmo método com diferentes
valores de entrada, evitando repetição de código.
'''
from parameterized import parameterized
'''
Cria uma classe de teste que herda de TestCase do Django
o que permite rodar testes com banco de
dados temporário e integração com o sistema de testes do Django.

Esse decorador executa o método test_first_name_placeholder_is_correct 
várias vezes, uma para cada par (field, placeholder) na lista.

Por exemplo:
Primeira execução: field = 'username', placeholder = 'Your username'
Segunda execução: field = 'email', placeholder = 'Your e-mail'
E assim por diante...
'''

class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Your username'),
        ('email', 'Your e-mail'),
        ('first_name', 'Ex:. John'),
        ('last_name', 'Ex:. Doe'),
        ('password', 'Type your password'),
        ('password2', 'Repeat your password'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()  # Cria uma instância do formulário
        current_placeholder = form[field].field.widget.attrs['placeholder']  # Pega o placeholder do campo
        self.assertEqual(current_placeholder, placeholder)  # Verifica se o valor está correto



