from orcamento import Orcamento, Item
from impostos import ICMS, ISS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orçamento: Orcamento, imposto) -> None:

        imposto_calculado = imposto.calcula(orçamento)

        print(imposto_calculado)


if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 500))
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())  # imprime 50.0
    calculador_de_impostos.realiza_calculo(orcamento, ISS())  # imprime 30.0
