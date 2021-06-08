from orcamento import Orcamento
from typing import Union


def calcula_ISS(orçamento: Orcamento) -> Union[int, float]:

    return orçamento.valor * 0.1


def calcula_ICMS(orçamento: Orcamento) -> Union[int, float]:

    return orçamento.valor * 0.06
