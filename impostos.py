from orcamento import Item


class ISS(object):
    def calcula(self, orçamento: Item) -> float:

        return orçamento.valor * 0.1


class ICMS(object):
    def calcula(self, orçamento: Item) -> float:

        return orçamento.valor * 0.06
