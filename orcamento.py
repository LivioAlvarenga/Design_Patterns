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

    EM_APROVAÇÃO: int = 1
    APROVADO: int = 2
    REPROVADO: int = 3
    FINALIZADO: int = 4

    def __init__(self) -> None:
        self.__itens: list = []
        self.estado_atual = Orcamento.EM_APROVAÇÃO
        self.__desconto_extra: float = 0

    def aplica_desconto_extra(self) -> None:
        if self.estado_atual == Orcamento.EM_APROVAÇÃO:
            self.__desconto_extra += self.valor * 0.02
        elif self.estado_atual == Orcamento.APROVADO:
            self.__desconto_extra += self.valor * 0.05
        elif self.estado_atual == Orcamento.REPROVADO:
            raise Exception(
                'Orçamentos reprovados não recebem desconto extra'
            )
        elif self.estado_atual == Orcamento.FINALIZADO:
            raise Exception(
                'Orçamentos finalizados não recebem desconto extra'
            )

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
        return total - self.__desconto_extra

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


if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    print(f'\nValor total do orçamento sem desconto é {orcamento.valor}')

    orcamento.estado_atual = Orcamento.APROVADO
    orcamento.aplica_desconto_extra()

    print(f'\nValor total do orçamento com desconto de é {orcamento.valor}')
