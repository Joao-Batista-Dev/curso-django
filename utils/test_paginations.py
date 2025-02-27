from unittest import TestCase # Importante Teste do Python - Teste consumir pouco cache
from utils.pagination import make_pagination_range # importando minha função de pagination

class PaginationTest(TestCase):
    # funcao teste pra retorna um range de paginação
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), # criando meu ranger e colocando em uma lista
            qty_paginas=4, # quantidade de paginas que queremos mostrar
            current_pages=1, # para saber em qual pagina estamos
        )

        self.assertEqual([1, 2, 3, 4], pagination) # assertEqual - Verificar se determinado valor de uma lista é igual - quando estamos fazendo Test Unitarios Unittest
    
    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        ...


