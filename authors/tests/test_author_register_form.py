# Importa a classe base de teste do Django.
# mais rapidos
from unittest import TestCase
# Importa a classe base de teste do Django.
# para usar outros tipos de teste no django
from django.test import TestCase as DjangoTestCase 
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
# importando nossa urls - para o teste de integração
from django.urls import reverse


# classe para Teste Unitarios
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


# classe para Teste Integração
class AuthorRegisterIntergrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anuyemail.com',
            'password': 'Ful@no1',
            'password2': 'Ful@no1',
        }

        return super().setUp(*args, **kwargs)
    
    # Teste nos campos de fields
    @parameterized.expand([
        ('username', 'Your username'),
        ('first_name', 'Ex:. John'),
        ('last_name', 'Ex:. Doe'),
        ('email', 'Your e-mail'),
        ('password', 'Type your password'),
        ('password2', 'Repeat your password')
    ])
    # verificar se o campo do formulario esta vazio
    def test_fields_connot_be_empty(self, field, msg):
        self.form_data['field'] = '' # dizendo que meu campo e vazio
        url = reverse('authors:create') # pegando url que eu quero
        reponse = self.client.post(url, data=self.form_data, follow=True) # enviar os dados necessarios para o nosso formulario
        self.assertIn(msg, reponse.content.decode('utf-8')) # verifcar se a messagem esta no forms

    def test_password_field_have_lower_upper_case_letters_and_numbers(self):
         self.form_data['password'] = 'abc123'
         url = reverse('authors:create')
         response = self.client.post(url, data=self.form_data, follow=True)
 
         msg = (
             'Password must have at least one uppercase letter, '
             'one lowercase letter and one number. The length should be '
             'at least 8 characters.'
         )
 
         self.assertIn(msg, response.context['form'].errors.get('password'))
         self.assertIn(msg, response.content.decode('utf-8'))
 
         self.form_data['password'] = '@A123abc123'
         url = reverse('authors:create')
         response = self.client.post(url, data=self.form_data, follow=True)
 
         self.assertNotIn(msg, response.context['form'].errors.get('password'))

    def test_password_and_password_confirmation_are_equal(self):
         self.form_data['password'] = '@A123abc123'
         self.form_data['password2'] = '@A123abc1235'
 
         url = reverse('authors:create')
         response = self.client.post(url, data=self.form_data, follow=True)
 
         msg = 'password and password2 must be equal!'
 
         self.assertIn(msg, response.context['form'].errors.get('password'))
         self.assertIn(msg, response.content.decode('utf-8'))
 
         self.form_data['password'] = '@A123abc123'
         self.form_data['password2'] = '@A123abc123'
 
         url = reverse('authors:create')
         response = self.client.post(url, data=self.form_data, follow=True)
 
         self.assertNotIn(msg, response.content.decode('utf-8'))
