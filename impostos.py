from orcamento import Orcamento
from abc import ABCMeta, abstractmethod


class Imposto(object):

    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orçamento) -> float:
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orçamento)

    @abstractmethod
    def calcula(self, orçamento: Orcamento) -> float:
        pass


class Template_de_imposto_condicional(Imposto):

    __metaclass__ = ABCMeta

    def calcula(self, orçamento: Orcamento) -> float:
        if self.deve_usar_maxima_taxacao(orçamento):
            return self.maxima_taxacao(orçamento) + (
                self.calculo_do_outro_imposto(orçamento)
            )
        else:
            return self.minima_taxacao(orçamento) + (
                self.calculo_do_outro_imposto(orçamento)
            )

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orçamento: Orcamento) -> bool:
        pass

    @abstractmethod
    def maxima_taxacao(self, orçamento: Orcamento) -> float:
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento: Orcamento) -> float:
        pass


def IPVX(método_ou_função):
    def empacotamento(self, orçamento: Orcamento):
        return método_ou_função(self, orçamento) + 50.0
    return empacotamento


class ISS(Imposto):

    @IPVX
    def calcula(self, orçamento: Orcamento) -> float:
        return orçamento.valor * 0.1 + (
            self.calculo_do_outro_imposto(orçamento)
        )


class ICMS(Imposto):

    def calcula(self, orçamento: Orcamento) -> float:
        return orçamento.valor * 0.06 + (
            self.calculo_do_outro_imposto(orçamento)
        )


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
