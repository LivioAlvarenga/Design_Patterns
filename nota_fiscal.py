from datetime import date
from typing import Any


class Item(object):

    def __init__(self, descrição: str, valor: float):
        self.__descrição = descrição
        self.__valor = valor

    @property
    def descrição(self):
        return self.__descrição

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal(object):

    def __init__(self,
                 razão_social: str,
                 cnpj: str,
                 itens: Any,
                 data_de_emissão: date = date.today(),
                 detalhes: str = '',
                 observadores: list = []
                 ):

        self.__razão_social = razão_social
        self.__cnpj = cnpj
        self.__data_de_emissão = data_de_emissão
        if len(detalhes) > 20:
            raise Exception(
                'Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

        # . Aplicando padrão observadores,
        for observador in observadores:
            observador(self)

    @property
    def razão_social(self):
        return self.__razão_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissão(self):
        return self.__data_de_emissão

    @property
    def detalhes(self):
        return self.__detalhes


# .Testando o código.
if __name__ == '__main__':

    from observadores import imprime_nf, envia_nf_por_email, salva_nf_no_banco

    itens = [Item('ITEM A', 100), Item('ITEM B', 200)]

    nota_fiscal = Nota_fiscal(
        detalhes='',
        razão_social='FUSA Limitada',
        cnpj='012345678901234',
        itens=itens,
        data_de_emissão=date.today(),
        observadores=[imprime_nf, envia_nf_por_email, salva_nf_no_banco]
    )

    print(f'\nNF sem método Builder\n\
        Razão social: {nota_fiscal.razão_social}\n\
        CNPF: {nota_fiscal.cnpj}\n\
        Data de emissão: {nota_fiscal.data_de_emissão}\n\
        Detalhes NF: {nota_fiscal.detalhes}')
