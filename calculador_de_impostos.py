from typing import Union
from orcamento import Orcamento
from impostos import calcula_ICMS, calcula_ISS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orçamento: Orcamento, imposto) -> None:

        imposto_calculado: Union[int, float] = 0

        imposto_calculado = imposto(orçamento)

        print(imposto_calculado)


if __name__ == '__main__':

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    # * Passando função como argumento, aplicado o padrão Strategy
    calculador.realiza_calculo(orcamento, calcula_ISS)
    calculador.realiza_calculo(orcamento, calcula_ICMS)
