<<<<<<< HEAD
from orcamento import Item


class ISS(object):
    def calcula(self, orçamento: Item) -> float:

        return orçamento.valor * 0.1


class ICMS(object):
    def calcula(self, orçamento: Item) -> float:

        return orçamento.valor * 0.06
=======
from orcamento import Orcamento
from typing import Union


def calcula_ISS(orçamento: Orcamento) -> Union[int, float]:

    return orçamento.valor * 0.1


def calcula_ICMS(orçamento: Orcamento) -> Union[int, float]:

    return orçamento.valor * 0.06
>>>>>>> 184f6d56bf7fe8ab2316ff7c95e5ead08f48c4a5
