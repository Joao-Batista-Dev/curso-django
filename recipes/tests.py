from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeURLsTest(TestCase): # classe de teste da minhas urls
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/') # verificando se url e barrar

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/') # verificando se url e barrar

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/') # verificando se url e barrar

class RecipeViewsTest(TestCase): # Classe de teste da minha views
    def test_recipe_home_view_function_is_correct(self): # verificando a função da minha home
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self): # verificando a função da minha categoria
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)
    
    def test_recipe_detail_view_function_is_correct(self): # verificando a função da minha recipe
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)