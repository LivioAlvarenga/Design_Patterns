from typing import Union
from abc import ABCMeta, abstractmethod


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
        self.__desconto_extra: float = 0
        self.estado_atual = Em_aprovacao()

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self) -> None:
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def valor(self) -> float:
        """Quando a propriedade for acessada, ela soma cada item retornando o valor
        do orçamento e aplica o desconto extra.

        Returns:
            float: Valor total do orçamento menos desconto extra.
        """
        total: float = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    @property
    def total_itens(self) -> int:
        """Conta total de itens do orçamento.

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
        """Adiciona itens a lista itens.

        Args:
            item (class Item): Recebe descrição do item e valor do mesmo
        """
        self.__itens.append(item)


class Estado_de_um_orcamento(object):
    """Classe abstrata com padrão Template Method. A classe filha que herdar será
    obrigada a implementar o método: aplica_desconto_extra(), aprova(),
    reprova() e finaliza().

    Returns:
        [Template Method]: Padrão Template Method nas classes filhas.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orçamento: Orcamento) -> float:
        """Método abstrato. Obrigatoriedade de implementação na classe filha.

        Args:
            orçameto (Class Orçamento): valor do orçamento.
        """
        pass

    @abstractmethod
    def aprova(self, orçamento: Orcamento):
        """Método abstrato. Obrigatoriedade de implementação na classe filha.

        Args:
            orçameto (Class Orçamento): valor do orçamento.
        """
        pass

    @abstractmethod
    def reprova(self, orçamento: Orcamento):
        """Método abstrato. Obrigatoriedade de implementação na classe filha.

        Args:
            orçameto (Class Orçamento): valor do orçamento.
        """
        pass

    @abstractmethod
    def finaliza(self, orçamento: Orcamento):
        """Método abstrato. Obrigatoriedade de implementação na classe filha.

        Args:
            orçameto (Class Orçamento): valor do orçamento.
        """
        pass


class Em_aprovacao(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orçamento: Orcamento):
        orçamento.adiciona_desconto_extra(orçamento.valor * 0.02)

    def aprova(self, orçamento):
        orçamento.estado_atual = Aprovado()

    def reprova(self, orçamento):
        orçamento.estado_atual = Reprovado()

    def finaliza(self, orçamento):
        raise Exception(
            'Orçamento em aprovação não podem ir para finalizado diretamente.')


class Aprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orçamento: Orcamento):
        orçamento.adiciona_desconto_extra(orçamento.valor * 0.05)

    def aprova(self, orçamento):
        raise Exception('Orçamento já esta aprovado.')

    def reprova(self, orçamento):
        raise Exception('Orçamento aprovado não pode ser reprovado.')

    def finaliza(self, orçamento):
        orçamento.estado_atual = Finalizado()


class Reprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orçamento: Orcamento) -> float:
        raise Exception('Orçamentos reprovados não recebem desconto extra.')

    def aprova(self, orçamento):
        raise Exception('Orçamento reprovado não pode ser aprovado.')

    def reprova(self, orçamento):
        raise Exception(
            'Orçamento reprovado não pode ser reprovado novamente.')

    def finaliza(self, orçamento):
        orçamento.estado_atual = Finalizado()


class Finalizado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orçamento: Orcamento) -> float:
        raise Exception('Orçamentos finalizados não recebem desconto extra.')

    def aprova(self, orçamento):
        raise Exception(
            'Orçamento finalizado não pode ser aprovado novamente.')

    def reprova(self, orçamento):
        raise Exception(
            'Orçamento finalizado não pode ser reprovado novamente.')

    def finaliza(self, orçamento):
        raise Exception(
            'Orçamento finalizado não pode ser finalizado novamente.')


# .Testando o código.
if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    print(f'\nValor total do orçamento sem desconto é {orcamento.valor}')

    orcamento.aprova()
    orcamento.reprova()

    # orcamento.aplica_desconto_extra()

    print(f'\nValor total do orçamento com desconto de é {orcamento.valor}')
