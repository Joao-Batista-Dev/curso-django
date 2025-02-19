from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase): # Classe de teste da minha views
   
    # setUP
    def test_recipe_home_view_function_is_correct(self): # verificando a função da minha home
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    # tearDown

    def test_recipe_home_views_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home')) # Usando o cliente do Django - Cliente virtual do django para teste
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_views_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home')) # Usando o cliente do Django - Cliente virtual do django para teste
        self.assertTemplateUsed(response, 'recipes/pages/home.html') # Retorna o nosso template que está sendo usado

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self): # Teste para verificar se temos receita na base de dados
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            response.content.decode('utf-8')
        ) # verificar se tem um determinado dado na nossa base do html

    # Teste para retorna nossa views com conteudo
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home')) # criando minha response
        content = response.content.decode('utf-8') # verifcando o conteudo do content
        response_context_recipes = response.context['recipes'] # Pegando os conteudo da minha recipe
        
        self.assertIn('Recipe Title', content) # Verificar se meu tile está no meu conteudo
        self.assertEquals(len(response_context_recipes), 1)
    # retorna a verificação se tem pagina - CATEGORIA
    def test_recipe_category_view_function_is_correct(self): # verificando a função da minha categoria
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    # verificar status code de error - CATEGORIA
    def test_recipe_category_views_404_if_no_recipes_fouund(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1})) # Usando o cliente do Django - Cliente virtual do django para teste
        self.assertEqual(response.status_code, 404)

    # retorna a verificação se tem pagina - CATEGORIA 
    def test_recipe_detail_view_function_is_correct(self): # verificando a função da minha recipe
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)
    
    # verificar status code de error - CATEGORIA
    def test_recipe_detail_views_404_if_no_recipes_fouund(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1})) # Usando o cliente do Django - Cliente virtual do django para teste
        self.assertEqual(response.status_code, 404)
    