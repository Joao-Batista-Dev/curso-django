from django.contrib.staticfiles.testing import StaticLiveServerTestCase # exercutar servido ativo - com css
from utils.browser import make_chrome_browser # importando nossa configuracao do selenium
import time
from recipes.tests.test_recipe_base import RecipeMixins # importando minha classe maxins

# classe base para codigos que seriam repetidos
class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixins):
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
