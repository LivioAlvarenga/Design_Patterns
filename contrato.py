from datetime import date


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


class Estado(object):

    def __init__(self, contrato: Contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        """Da acesso ao contrato da class Contrato

        Returns:
            class Contrato: Objeto class Contato
        """
        return self.__contrato


class Historico(object):

    def __init__(self):
        self.__estados_salvos: list = []

    def obtém_estado(self, indice: int):
        """Consulta o historico dos contratatos em uma list atreves de um indice.

        Returns:
            class Contrato: Objeto class Contato especifico.
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

    print(f'\nContrato: \n\
        Cliente: {contrato.cliente}\n\
        Data: {contrato.data}\n\
        Tipo: {contrato.tipo}')

    contrato.avança()

    print(f'\nContrato: \n\
        Cliente: {contrato.cliente}\n\
        Data: {contrato.data}\n\
        Tipo: {contrato.tipo}')
