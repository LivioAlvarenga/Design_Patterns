from orcamento import Orcamento


class ISS(object):

    def calcula(self, orçamento: Orcamento) -> float:

        return orçamento.valor * 0.1


class ICMS(object):

    def calcula(self, orçamento: Orcamento) -> float:

        return orçamento.valor * 0.06


class ICPP(object):

    def calcula(self, orçamento: Orcamento) -> float:
        if orçamento.valor > 500:
            return orçamento.valor * 0.07
        else:
            return orçamento.valor * 0.05


class IKCV(object):

    def calcula(self, orçamento: Orcamento) -> float:
        if orçamento.valor > 500 and (
            self.__tem_item_maior_que_100_reais(orçamento)
        ):
            return orçamento.valor * 0.10
        else:
            return orçamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orçamento: Orcamento) -> bool:
        for item in orçamento.obter_itens():
            if item.valor > 100:
                return True
        return False
