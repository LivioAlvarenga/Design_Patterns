from typing import Union


class Orcamento(object):

    def __init__(self, valor) -> None:

        self.__valor: Union[int, float] = valor

    @property
    def valor(self) -> Union[int, float]:
        """Dar acesso a variavel privada __valor como propriedade.
        Ex: orçamento_a = Orçamento(500)
        orçamento_a.valor

        Returns:
            [int, float]: Leitura de valor no formato int ou float
        """
        return self.__valor
