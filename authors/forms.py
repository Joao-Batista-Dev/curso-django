#from django.forms import Form, ModelForm
from django import forms # import forms
from django.contrib.auth.models import User # import models Users

# criando forms atrelado ao models existente
class RegisterForm(forms.ModelForm):
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