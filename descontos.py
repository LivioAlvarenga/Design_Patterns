from typing import Literal
from orcamento import Orcamento


class Desconto_por_cinco_itens(object):

    def __init__(self, proximo_desconto) -> None:
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orçamento: Orcamento) -> float:
        if orçamento.total_itens > 5:
            return orçamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orçamento)


class Desconto_por_mais_de_quinhentos_reais(object):

    def __init__(self, proximo_desconto) -> None:
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orçamento: Orcamento) -> float:
        if orçamento.valor > 500:
            return orçamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orçamento)


class Sem_desconto(object):

    def calcula(self, orçamento: Orcamento) -> Literal[0]:
        return 0
