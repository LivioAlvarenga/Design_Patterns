from typing import Dict, List, Union

# ! BOAS PRATICAS COM PEP-8

"""
- Cases Styles:
    Existe 4 boas praticas para utilizar:
        camelCase
        PascalCase (usado comumente para nomes de Class)
        snake_case (usado comumente para nomes de variaveis)
        kebab-case (usado mais em URLs)
"""


"""
- Constantes:
    01. Usa snake_case com caixa alta.
        COD_PADRÃO = 'PR'
    02. É boa prática colocar um arquivo .py com nome de constantes e colocar
        todas neste arquivo.
"""


"""
- Variaveis:
    01. Informar a tipagem que a variavel ira deve receber.
        x: int = 1
        y: str = 'Hello'
    02. Usar o formato snake_case nos nomes de variáveis
        clientesatendidos seria clientes_atendidos

"""

# *ex:01 - Colocamos apos a variavel o que a mesma recebe

x: int = 1
y: str = 'Hello Word'

# Estamos informando que esta variavel é uma lista com str.
lista: List[str] = []
lista1: List[Union[float, int]] = []

# Estamos informando que esta variavel é um dict com key str é value int.
dicionario: Dict[str, int] = {}

# Estamos informando que esta variavel é um dict com key str e o value pode
#   ser um list str, str ou int. Usamos o Union para isso.
dicionario2: Dict[str, Union[List[str], str, int]] = {}


"""
- Funções:

    01. Usar Type Hints, Colocar ao finalizar uma função o que a mesma retorna:
        def soma_numeros()->None:
            x + y

"""

# *ex:01 - Informamos o retorno da função (Type Hint).


def soma_numeros(x: int, y: int) -> None:
    x + y


def soma_numeros_com_retorno(x: int, y: int) -> int:
    total: int = x + y
    return total


"""
- Classes:

    01. Usar formato PascalCase para facilitar a leitura:
        Class AtenderCliente:

"""
