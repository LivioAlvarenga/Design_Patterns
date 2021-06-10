from orcamento import Orcamento, Item
from impostos import ICMS, ISS, ICPP, IKCV


class Calculador_de_impostos(object):

    def realiza_calculo(self, orçamento: Orcamento, imposto) -> None:

        imposto_calculado = imposto.calcula(orçamento)

        print(imposto_calculado)


if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 500))
    calculador_de_impostos = Calculador_de_impostos()

    print('\nISS e ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

    # > Calcular impostos juntos
    print('\nISS com ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS(ICMS()))

    print('\nICPP e IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())

    # > Calcular impostos juntos
    print('\nICPP com IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP(IKCV()))
