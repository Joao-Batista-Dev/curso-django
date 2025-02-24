from django.test import TestCase
from django.urls import reverse
from unittest import skip

class RecipeURLsTest(TestCase): # classe de teste da minhas urls
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/') # verificando se url e barrar

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/') # verificando se url e barrar

    @skip()
    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/') # verificando se url e barrar

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:search',)
        self.assertEqual(url, '/recipes/search/') # verificando se url e barrar

    