from orcamento import Orcamento


class ISS(object):
    def calcula(self, orçamento: Orcamento) -> float:

        return orçamento.valor * 0.1


class ICMS(object):
    def calcula(self, orçamento: Orcamento) -> float:

        return orçamento.valor * 0.06
