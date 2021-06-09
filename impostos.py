from orcamento import Orcamento
from typing import Union


class ISS(object):
    def calcula(self, orçamento: Orcamento) -> Union[int, float]:

        return orçamento.valor * 0.1


class ICMS(object):
    def calcula(self, orçamento: Orcamento) -> Union[int, float]:

        return orçamento.valor * 0.06
