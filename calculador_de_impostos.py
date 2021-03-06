from orcamento import Orcamento, Item
from impostos import ICMS, ISS, ICPP, IKCV


class Calculador_de_impostos(object):

    def realiza_calculo(self, orçamento: Orcamento, imposto) -> None:
        """Realiza o cálculo de impostos no orçamento. Duck Typing o atributo
        imposto é uma class imposto que deve ter um método calcula.

        Args:
            orçameto (Class Orçamento): valor do orçamento.
            imposto (Classes impostos.py): % de imposto a ser calculado.
        """
        imposto_calculado: float = imposto.calcula(orçamento)

        print(imposto_calculado)


# .Testando o código.
if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 500))
    calculador_de_impostos = Calculador_de_impostos()

    print('\nISS e ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

    # .Calcular impostos juntos
    print('\nISS com ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS(ICMS()))

    print('\nICPP e IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())

    # .Calcular impostos juntos
    print('\nICPP com IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP(IKCV()))
