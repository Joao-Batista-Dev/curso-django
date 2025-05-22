from django.views import View
from recipes.models import Recipe
from django.contrib import messages
from django.http.response import Http404
from authors.forms.recipe_form import AuthorRecipeForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='authors:login', redirect_field_name='next'), name='dispatch')
class DashboardRecipe(View):
    def get_recipe(self, request, id=None):
        recipe = None

        if id is not None:
            recipe = Recipe.objects.filter(
                is_published=False,
                author=request.user,
                pk=id
            ).first()

            if not recipe:
                raise Http404()
        
        return recipe


    def get(self, id=None):
        recipe = self.get_recipe(id)

        form = AuthorRecipeForm(instance=recipe) 

        return self.render_recipe(form)
    

    def post(self, request, id=None):
        recipe = self.get_recipe(id)

        form = AuthorRecipeForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=recipe
        ) 

        if form.is_valid():
            recipe = form.save(commit=False)

            recipe.author = request.user
            recipe.preparation_steps_is_html = False
            recipe.is_published = False

            recipe.save()

            messages.success(
                request, 
                'Sua receita foi salva com sucesso!'
            )

            return redirect(reverse('authors:dashboard_recipe_edit', args=(recipe.id,)))

        return self.render_recipe(form)


    def render_recipe(self, form):
        return render(
            self.request, 
            'authors/pages/dashboard_recipe.html',
            {
                'form':form
            }
        )
        



