from orcamento import Orcamento
from abc import ABCMeta, abstractmethod


class Imposto(object):

    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto=None):
        """Construtor criado para chamar o outro imposto aplicando a soma de
        impostos aplicando o padrão Decorator. Um imposto chamaria o outro
        imposto. Ex: ISS(ICMS()) outro_imposto = ICMS()

        Args:
            outro_imposto (classes de imposto.py): Classes de imposto.py.
            Valor padrão = None
        """
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orçamento: Orcamento) -> float:
        """Faz calculo do outro imposto.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            float: 0 (Zero) if imposto = None ou valor do imposto informado.
        """
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orçamento)

    @abstractmethod
    def calcula(self, orçamento: Orcamento) -> float:
        """Método abstrato. Obrigatoriedade de implementação na classe filha.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            float: Retornara o calculo do imposto de acordo com cada regra da
            classe filha.
        """
        pass


class Template_de_imposto_condicional(Imposto):
    """Classe abstrata com padrão Template Method. A classe filha que herdar será
    obrigada a implementar os metodos: deve_usar_maxima_taxacao(),
    maxima_taxacao() e minima_taxacao().

    Args:
        Imposto (class Imposto): Herda Classe abstrata imposto.
        Obrigatoriedade de implementação do método calcula()

    Returns:
        [Template Method]: Padrão Template Method nas classes filhas.
    """

    __metaclass__ = ABCMeta

    def calcula(self, orçamento: Orcamento) -> float:
        """Calcula o imposto entre maxima e mínima taxação. Método obrigatório
        herdado da class Imposto. Soma com outro imposto caso seja informado.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            float: Retorna calculo do imposto ou imposto + outro imposto.
        """
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
        """Método abstrato. Obrigatoriedade de implementação na classe filha.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            bool: Retornara um bool de acordo com cada regra da classe filha.
        """
        pass

    @abstractmethod
    def maxima_taxacao(self, orçamento: Orcamento) -> float:
        """Método abstrato. Obrigatoriedade de implementação na classe filha.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            float: Retornara um desconto maximo de acordo com cada regra da
            classe filha.
        """
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento: Orcamento) -> float:
        """Método abstrato. Obrigatoriedade de implementação na classe filha.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            float: Retornara um desconto mínimo de acordo com cada regra da
            classe filha.
        """
        pass


def IPVX(método_ou_função):
    """Padrão decorator, soma 50,00 ao imposto que receber este decorator.

    Args:
        (método ou função): método ou função de uma determinada class
    """

    def empacotamento(self, orçamento: Orcamento) -> float:
        """Empacota o valor de 50,00 no método ou função que tiver o decorator IPVX()

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            [float]: valor de imposto + 50,00
        """
        return método_ou_função(self, orçamento) + 50.0
    return empacotamento


class ISS(Imposto):
    """Responsável por calcular o imposto ISS.

    Args:
        Imposto (class): Herda Classe abstrata, obrigatoriedade de
        implementação do método calcula().
    """

    @IPVX
    def calcula(self, orçamento: Orcamento) -> float:
        """Método abstrato. Calcula imposto ISS com decorator IPVX.

        Args:
            orçameto (Class Orçamento): valor do orçamento.
            IPVX (método): soma 50,00

        Returns:
            float: Retornara o calculo do imposto + Decorator IPVX
        """
        return orçamento.valor * 0.1 + (
            self.calculo_do_outro_imposto(orçamento)
        )


class ICMS(Imposto):
    """Responsável por calcular o imposto ICMS.

    Args:
        Imposto (class): Herda Classe abstrata, obrigatoriedade de
        implementação do método calcula().
    """

    def calcula(self, orçamento: Orcamento) -> float:
        return orçamento.valor * 0.06 + (
            self.calculo_do_outro_imposto(orçamento)
        )


class ICPP(Template_de_imposto_condicional):
    """Responsável por calcular o imposto ICPP.

    Args:
        Template_de_imposto_condicional (class): Herda Classe abstrata,
        obrigatoriedade de implementação dos métodos deve_usar_maxima_taxacao()
        maxima_taxacao() e minima_taxacao().
    """

    def deve_usar_maxima_taxacao(self, orçamento: Orcamento) -> bool:
        return orçamento.valor > 500

    def maxima_taxacao(self, orçamento: Orcamento) -> float:
        return orçamento.valor * 0.07

    def minima_taxacao(self, orçamento: Orcamento) -> float:
        return orçamento.valor * 0.05


class IKCV(Template_de_imposto_condicional):
    """Responsável por calcular o imposto IKCV.

    Args:
        Template_de_imposto_condicional (class): Herda Classe abstrata,
        obrigatoriedade de implementação dos métodos deve_usar_maxima_taxacao()
        maxima_taxacao() e minima_taxacao().
    """

    def deve_usar_maxima_taxacao(self, orçamento: Orcamento) -> bool:
        return orçamento.valor > 500 and (
            self.__tem_item_maior_que_100_reais(orçamento)
        )

    def maxima_taxacao(self, orçamento: Orcamento) -> float:
        return orçamento.valor * 0.10

    def minima_taxacao(self, orçamento: Orcamento) -> float:
        return orçamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orçamento: Orcamento) -> bool:
        """Método privado que verifica se existe algum item do orçamento maior
        que 100,00.

        Args:
            orçameto (Class Orçamento): valor do orçamento.

        Returns:
            bool: True if R$ item > 100,00 else False
        """
        for item in orçamento.obter_itens():
            if item.valor > 100:
                return True
        return False
