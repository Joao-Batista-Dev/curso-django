from django.test import TestCase
from recipes.models import Recipe, Category, User # Importando minhas tabelas

# criando minha classe mixins
class RecipeMixins():
    def make_recipe(self, name='Category'):
        return Category.objects.create(name=name) # Criando nossa categoria
    
    def make_author(
            self,
            first_name='fulano',
            last_name='detal',
            username='fulano',
            password='123456',
            email='fulanodetal@gmail.com', 
        ):
        return User.objects.create_user( # criando o meu usuario com o usuario do django
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_category(
            self, 
            category_data=None,
            author_data=None,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        ):

        if category_data is None:
            category_data = {}

        if author_data is None: 
            author_data = {}

        return Recipe.objects.create( # criando minha receitas
            category=self.make_category(**category_data),
            author_data=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
    
    def make_recipe_in_batch(self, qtd=10):
        recipes = []

        for i in range(qtd):
            kwargs = {'slug': f'r{i}', 'authors_data': {'username': f'u{i}'}}
            recipe = self.make_recipe(**kwargs)
            recipes.append(recipe)

        return recipes


# minha classe utilizando mais de uma heranca
class RecipeTestBase(TestCase, RecipeMixins):
    def setUp(self) -> None: # exercutado antes de todos os teste
        return super().setUp()
    
    