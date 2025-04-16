#from django.forms import Form, ModelForm
from django import forms # import forms
from django.contrib.auth.models import User # import models Users

# criando forms atrelado ao models existente
class RegisterForm(forms.ModelForm):
    # outra forma de sobreescrever campos do formulario
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex:. John'
        }),
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex:. Doe'
        }),
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name'
        }),
    )

    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your e-mail'
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password'
        }),
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        }),
    )

    # criamos uma meta classe
    # paar passamos meta dados
    class Meta:
        # models que vamos usar
        model = User 
        # campos do formulario que queremos
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ] 