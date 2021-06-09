from typing import Union


class Item(object):

    def __init__(self, nome: str, valor: Union[int, float]) -> None:
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self) -> str:
        """Dar acesso a variavel privada __nome como propriedade.

        Returns:
            [int, float]: Leitura de valor no formato int ou float
        """
        return self.__nome

    @property
    def valor(self) -> Union[int, float]:
        """Dar acesso a variavel privada __valor como propriedade.
        Ex: orçamento_a = Orçamento(500)
        orçamento_a.valor

        Returns:
            [int, float]: Leitura de valor no formato int ou float
        """
        return self.__valor


class Orcamento(object):

    def __init__(self) -> None:
        self.__itens: list = []

    @property
    def valor(self) -> float:
        """Quando a propriedade for acessada, ela soma cada item retornando o valor
            do orçamento

        Returns:
            float: Valor total do orçamento
        """
        total: float = 0.0
        for item in self.__itens:
            total += item.valor
        return total

    @property
    def total_itens(self) -> int:
        """Conta total de itens do orçamento

        Returns:
            int: Quantidade total de itens do orçamento
        """
        return len(self.__itens)

    def obter_itens(self) -> tuple:
        """Transforma a lista de itens em uma tupla.

        Returns:
            tuple: Tupla com os itens.
        """
        return tuple(self.__itens)

    def adiciona_item(self, item: Item):
        """Adiciona itens a lista itens

        Args:
            item ([type]): [description]
        """
        self.__itens.append(item)
