from orcamento import Orcamento


class Calculador_de_impostos(object):

    def realiza_calculo(self, orçamento: Orcamento, imposto) -> None:

        if imposto == 'ICMS':
            imposto_calculado = orçamento.valor * 0.1

        elif imposto == 'ISS':
            imposto_calculado = orçamento.valor * 0.06

        print(imposto_calculado)


if __name__ == '__main__':

    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, 'ICMS')  # imprime 50.0
    calculador_de_impostos.realiza_calculo(orcamento, 'ISS')  # imprime 30.0
