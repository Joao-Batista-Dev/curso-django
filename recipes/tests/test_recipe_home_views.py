from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest import skip # importando o skip para pular o teste


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

        self.fail('Fazendo o teste falhar') # falhando teste
        needed_title = 'This is a category test'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title, content)
    
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
    
    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It load one recipe'

        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1
                }
            )
        )
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        # Check if one recipe exists
        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_search_uses_correct_views_function(self):
        resolved = resolve(reverse('recipes:search',))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )