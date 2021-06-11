from datetime import date
from typing import Any


class Contrato(object):

    def __init__(self, data: date, cliente: str, tipo: str = "NOVO"):
        self.__data = data
        self.__cliente = cliente.capitalize()
        self.__tipo = tipo.upper()

    @property
    def data(self) -> date:
        """Da acesso a Data do contrato. Contrato.data"""
        return self.__data

    @data.setter
    def data(self, data: date):
        """Edita a data do contrato. Contrato.data(nova data)"""
        self.__data = data

    @property
    def cliente(self) -> str:
        """Da acesso ao Cliente do contrato. Contrato.cliente"""
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: str):
        """Edita Cliente do contrato. Contrato.cliente(novo cliente)"""
        self.__cliente = cliente.capitalize()

    @property
    def tipo(self) -> str:
        """Da acesso ao Tipo do contrato, sendo: Novo, Em Andamento, Acertado
        e Concluido"""
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        """Edita o acesso ao Tipo do contrato, sendo: Novo, Em Andamento, Acertado
        e Concluido"""
        self.__tipo = tipo.upper()

    def avança(self):
        """Avança o tipo do contrato na sequencia: Novo, Em Andamento,
        Acertado e Concluido"""

        if self.__tipo == 'NOVO':
            self.__tipo = 'EM ANDAMENTO'
        elif self.__tipo == 'EM ANDAMENTO':
            self.__tipo = 'ACERTADO'
        elif self.__tipo == 'ACERTADO':
            self.__tipo = 'CONCLUIDO'

    def salva_estado(self):
        """Cria um estado com espelho do contrato atual Obs. Um novo objeto,
        pois o mesmo será salvo no historico.

        Returns:
            Class Estado: Um objeto class Estado (class Contrato)
        """
        return Estado(Contrato(data=self.__data,
                               cliente=self.__cliente,
                               tipo=self.__tipo))

    def restaura_estado(self, estado: Any):
        """Restaura um contrato com os dados do estado (class Estado()).

        Args:
            estado (class Estado): class Estado contendo historico de um
            objeto Contrato()
        """
        self.__cliente = estado.contrato.cliente
        self.__data = estado.contrato.data
        self.__tipo = estado.contrato.tipo


class Estado(object):

    def __init__(self, contrato: Contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        """Da acesso ao contrato da class Contrato

        Returns:
            class Contrato: Objeto class Contrato
        """
        return self.__contrato


class Historico(object):

    def __init__(self):
        self.__estados_salvos: list = []

    @property
    def estados_salvos(self):
        """Da acesso a lista de contratos salvos.

        Returns:
            Lista de contrato [list]: Objeto class Contrato
        """
        return self.__estados_salvos

    def obtém_estado(self, indice: int):
        """Consulta o historico dos contratatos em uma list atreves de um indice.

        Returns:
            class Contrato: Objeto class Contrato especifico.
        """
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado: Estado):
        """Adiciona em uma list um Estado do contrato no historico dos
        contratatos."""
        self.__estados_salvos.append(estado)


if __name__ == '__main__':

    historico = Historico()

    contrato = Contrato(data=date.today(),
                        cliente='Flávio Almeida')

    print('\n1º Contrato')

    print(f'\nContrato: \n\
        Cliente: {contrato.cliente}\n\
        Data: {contrato.data}\n\
        Tipo: {contrato.tipo}')

    contrato.avança()

    print('\nContrato apos avançar')

    print(f'\nContrato: \n\
        Cliente: {contrato.cliente}\n\
        Data: {contrato.data}\n\
        Tipo: {contrato.tipo}')

    # .Adicionando historicos
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avança()

    historico.adiciona_estado(contrato.salva_estado())

    contrato.avança()

    # .Contrato mudou cliente
    contrato.cliente = 'Livio Alvarenga'

    historico.adiciona_estado(contrato.salva_estado())

    # .Restaurando contratos
    print('\nContratos restaurados.')

    for indice in range(len(historico.estados_salvos)):

        contrato.restaura_estado(historico.obtém_estado(indice))

        print(f'\nContrato: \n\
            Cliente: {contrato.cliente}\n\
            Data: {contrato.data}\n\
            Tipo: {contrato.tipo}')

# ! Padrão de projeto Memento
'''Agora temos uma maneira eficiente de salvar estados de um objeto, e
restaurá-los caso necessário. Sempre que temos um problema como esse, fazemos
uso do Memento. O Memento é um padrão de projeto que nos ajuda a salvar e
restaurar estados de objetos.

Um possível problema é a quantidade de memória que ele pode ocupar, afinal
estamos guardando muitas instâncias de objetos que podem ser pesados. Por isso,
dependendo do tamanho dos seus objetos, a classe Estado pode passar a guardar
não o objeto todo, mas sim somente as propriedades que mais fazem sentido.
Nada impede você também de limitar a quantidade máxima de objetos no histórico
que será armazenado.'''
