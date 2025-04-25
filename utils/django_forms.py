from django.core.exceptions import ValidationError
import re

# funcao para validar determinado campo
def strong_password(password):
    # verificar se minha senha e: A - Z: a-z: 0-9: 8 caracteres
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    # verificar se a regez da meth com a minha estring que o password 
    if not regex.match(password):
        # levantando o error
        raise ValidationError((
             'Password must have at least one uppercase letter, '
             'one lowercase letter and one number. The length should be '
             'at least 8 characters.'
         ),
             code='invalid'
         )
