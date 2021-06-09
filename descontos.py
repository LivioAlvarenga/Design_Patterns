from orcamento import Orcamento


class Desconto_por_cinco_itens(object):

    def calcula(self, orçamento: Orcamento) -> float:
        if orçamento.total_itens > 5:
            return orçamento.valor * 0.1
        else:
            return 0


class Desconto_por_mais_de_quinhentos_reais(object):

    def calcula(self, orçamento: Orcamento) -> float:
        if orçamento.valor > 500:
            return orçamento.valor * 0.07
        else:
            return 0
