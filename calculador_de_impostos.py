from orcamento import Orcamento
from impostos import calcula_ICMS, calcula_ISS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orçamento: Orcamento, imposto) -> None:

        imposto_calculado = imposto(orçamento)

        print(imposto_calculado)


if __name__ == '__main__':

    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(
        orcamento, calcula_ICMS)  # imprime 50.0
    calculador_de_impostos.realiza_calculo(
        orcamento, calcula_ISS)  # imprime 30.0
