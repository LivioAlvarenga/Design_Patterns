from orcamento import Orcamento, Item
from descontos import (
    Desconto_por_cinco_itens,
    Desconto_por_mais_de_quinhentos_reais,
    Sem_desconto
)


class Calculador_de_descontos(object):

    def calcula(self, orçamento: Orcamento) -> float:
        """Realiza o cálculo de descontos no orçamento com padrão Chain of
        Responsibility. A variavel desconto recebe as classes de desconto.py.
        O calculo é executado em cadeia um desconto chama o proximo ate chega
        a Sem_desconto().

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            float: Valor do desconto
        """
        desconto: float = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
        ).calcula(orçamento)

        return desconto


# .Testando o código.
if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 40))
    orcamento.adiciona_item(Item('ITEM - 4', 100))
    orcamento.adiciona_item(Item('ITEM - 5', 100))
    orcamento.adiciona_item(Item('ITEM - 6', 100))

    print(f'\nValor total do orçamento {orcamento.valor}')

    calculador_desconto = Calculador_de_descontos()

    desconto = calculador_desconto.calcula(orcamento)

    print(f'\nDesconto calculado de {desconto:.2f}')
