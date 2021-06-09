from typing import Optional
from orcamento import Orcamento, Item


class Calculador_de_descontos(object):

    def calcula(self, orçamento: Orcamento) -> Optional[float]:

        if orçamento.total_itens > 5:
            return orçamento.valor * 0.1

        elif orçamento.valor > 500:
            return orçamento.valor * 0.07

        return None


if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    print(f'Valor total do orçamento {orcamento.valor}')

    calculador_desconto = Calculador_de_descontos()

    desconto = calculador_desconto.calcula(orcamento)

    print(f'Desconto calculado de {desconto:.2f}')
