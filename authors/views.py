from django.shortcuts import render
from .forms import RegisterForm # importando meu forms


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(
        request, 
        'authors/pages/register_view.html',
        {
            'form': form,
        },
    )
