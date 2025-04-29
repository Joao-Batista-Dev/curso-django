from selenium.webdriver.common.by import By # para pegamos dados HTML
from .base import RecipeBaseFunctionalTest # importando arquivo de teste base

# classe que herda nossos metodos da classe base - codigos que seriam repetidos
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    # nosso teste
    def test_recipe_home_page_without_recipes_not_found_message(self): 
        self.browser.get(self.live_server_url) # pegando a url do nosso webdriver sem saber qual e

        self.sleep(6) # pausa o site por um determinado tempo

        body = self.browser.find_element(By.TAG_NAME, 'body') # para encontrar um elemento HTML com determinada classe, id, tag, texto, etc.
        self.assertIn('No recipes found here 🥲', body.text) # verificar se o texto esta no meu site
        
       
