from typing import Union


class Orcamento(object):

    def __init__(self, valor) -> None:

        self.__valor: Union[int, float] = valor

    @property
    def valor(self) -> Union[int, float]:
        """
        Método criado para dar acesso ao usuário da variavel privada __valor.

        Returns:
            - __valor: int, float
        """
        return self.__valor
