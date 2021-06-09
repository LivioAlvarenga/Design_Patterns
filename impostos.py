from orcamento import Orcamento
from abc import ABCMeta, abstractmethod


class Template_de_imposto_condicional(object):

    __metaclass__ = ABCMeta

    def calcula(self, orçamento: Orcamento):
        if self.deve_usar_maxima_taxacao(orçamento):
            return self.maxima_taxacao(orçamento)
        else:
            return self.minima_taxacao(orçamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento: Orcamento) -> bool:
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento: Orcamento) -> float:
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento: Orcamento) -> float:
        pass


class ISS(object):

    def calcula(self, orçamento: Orcamento) -> float:

        return orçamento.valor * 0.1


class ICMS(object):

    def calcula(self, orçamento: Orcamento) -> float:

        return orçamento.valor * 0.06


class ICPP(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orçamento) -> bool:
        return orçamento.valor > 500

    def maxima_taxacao(self, orçamento) -> float:
        return orçamento.valor * 0.07

    def minima_taxacao(self, orçamento) -> float:
        return orçamento.valor * 0.05


class IKCV(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orçamento) -> bool:
        return orçamento.valor > 500 and (
            self.__tem_item_maior_que_100_reais(orçamento)
        )

    def maxima_taxacao(self, orçamento) -> float:
        return orçamento.valor * 0.10

    def minima_taxacao(self, orçamento) -> float:
        return orçamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orçamento: Orcamento) -> bool:
        for item in orçamento.obter_itens():
            if item.valor > 100:
                return True
        return False
