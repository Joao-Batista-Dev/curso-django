from django.test import LiveServerTestCase # importando teste do servidor ativo - aparecer coisas na tela - executar o site sem css
from django.contrib.staticfiles.testing import StaticLiveServerTestCase # exercutar servido ativo - com css
from utils.browser import make_chrome_browser # importando nossa configuracao do selenium
import time
from selenium.webdriver.common.by import By # para pegamos dados HTML

# classe base para codigos que seriam repetidos
class RecipeBaseFunctionalTest(StaticLiveServerTestCase):
    # metodo responsavel - criar o browser
    def setUp(self) -> None:
        self.browser = make_chrome_browser('--headless') # criar o nosso browser - sempre criar um browser
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit() # parar fechar o nosso webdriver - sempre fechamos um browser
        return super().tearDown()
    
     # parar o site por um determinado tempo
    def sleep(self, seconds=5):
        time.sleep(seconds)

# classe que herda nossos metodos da classe base - codigos que seriam repetidos
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    # nosso teste
    def test_recipe_home_page_without_recipes_not_found_message(self): 
        self.browser.get(self.live_server_url) # pegando a url do nosso webdriver sem saber qual e

        self.sleep(6) # pausa o site por um determinado tempo

        body = self.browser.find_element(By.TAG_NAME, 'body') # para encontrar um elemento HTML com determinada classe, id, tag, texto, etc.
        self.assertIn('No recipes found here 🥲', body.text) # verificar se o texto esta no meu site
        
       
