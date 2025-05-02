from selenium.webdriver.common.by import By # para pegamos dados HTML
from .base import RecipeBaseFunctionalTest # importando arquivo de teste base
import pytest # importando o meu pystest - para usar o 'markers'
from unittest.mock import patch
from selenium.webdriver.common.keys import Keys

# classe que herda nossos metodos da classe base - codigos que seriam repetidos
# marcando meu teste
@pytest.mark.functionals_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    # nosso teste
    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_home_page_without_recipes_not_found_message(self): 
        self.browser.get(self.live_server_url) # pegando a url do nosso webdriver sem saber qual e

        self.sleep() # pausa o site por um determinado tempo

        body = self.browser.find_element(By.TAG_NAME, 'body') # para encontrar um elemento HTML com determinada classe, id, tag, texto, etc.
        self.assertIn('No recipes found here 🥲', body.text) # verificar se o texto esta no meu site
        
    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch()
 
        title_needed = 'This is what I need'
 
        recipes[0].title = title_needed
        recipes[0].save()
 
        # Usuário abre a página
        self.browser.get(self.live_server_url)
 
        # Vê um campo de busca com o texto "Search for a recipe"
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe"]'
         )
 
        # Clica neste input e digita o termo de busca
        # para encontrar a receita o título desejado
        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)
 
        # O usuário vê o que estava procurando na página
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME, 'main-content-list').text,
         )
