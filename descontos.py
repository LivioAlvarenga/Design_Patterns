from typing import Literal
from orcamento import Orcamento


class Desconto_por_cinco_itens(object):

    def __init__(self, proximo_desconto) -> None:
        """Construtor criado para chamar o proximo desconto fazendo descontos
        em cadeia padrão Chain of Responsibility. Um desconto chamaria o
        proximo desconto. Ex: Desconto_por_cinco_itens(Sem_desconto())
        proximo_desconto = Sem_desconto()

        Args:
            proximo_desconto (classes de desconto.py): Classes de descontos.py
        """
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orçamento: Orcamento) -> float:
        """Calcula se total de itens > 5 da desconto. Se não chama o proximo
        desconto da cadeia.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            float: Desconto ou  Proximo desconto das classes de desconto.py
        """
        if orçamento.total_itens > 5:
            return orçamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orçamento)


class Desconto_por_mais_de_quinhentos_reais(object):

    def __init__(self, proximo_desconto) -> None:
        """Construtor criado para chamar o proximo desconto fazendo descontos
        em cadeia padrão Chain of Responsibility. Um desconto chamaria o
        proximo desconto. Ex: Desconto_por_cinco_itens(Sem_desconto())
        proximo_desconto = Sem_desconto()

        Args:
            proximo_desconto (classes de desconto.py): Classes de Descontos.py
        """
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orçamento: Orcamento) -> float:
        """Calcula se total de orçamento > 500,00 da desconto. Se não chama o proximo
        desconto da cadeia.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            float: Desconto ou  Proximo desconto das classes de desconto.py
        """
        if orçamento.valor > 500:
            return orçamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orçamento)


class Sem_desconto(object):

    def calcula(self, orçamento: Orcamento) -> Literal[0]:
        """Criado para finalizar a cadeia de descontos, se passar por todos os
        descontos e nenhum for considerado o desconto é igual a zero
        finaliando a cadeia de descontos.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            Literal[0]: Retorna 0 (zero)
        """
        return 0
