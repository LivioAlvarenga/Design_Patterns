class Numero(object):

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


class Subtração(object):

    def __init__(self, expressão_esquerda, expressão_direita):
        self.__expressão_esquerda = expressão_esquerda
        self.__expressão_direita = expressão_direita

    def avalia(self):
        return (self.__expressão_esquerda.avalia()
                - self.__expressão_direita.avalia())


class Soma(object):

    def __init__(self, expressão_esquerda, expressão_direita):
        self.__expressão_esquerda = expressão_esquerda
        self.__expressão_direita = expressão_direita

    def avalia(self):
        return (self.__expressão_esquerda.avalia()
                + self.__expressão_direita.avalia())


if __name__ == '__main__':

    expressão_esquerda = Subtração(Numero(10), Numero(5))
    expressão_direita = Soma(Numero(2), Numero(10))
    expressão_conta = Soma(expressão_esquerda, expressão_direita)

    resultado = expressão_conta.avalia()
    print(resultado)

# !Padrão Interpreter
'''Veja que nossa árvore consegue interpretar, e calcular o resultado final.
Quando temos expressões que devem ser avaliadas, e a transformamos em uma
estrutura de dados, e depois fazemos com que a própria árvore se avalie, damos
o nome de Interpreter. O padrão é bastante útil quando temos que implementar
interpretadores para DSLs, ou coisas similares. É um padrão bem complicado, mas
bastante interessante. É comum que, ao ler a string (como por exemplo 2+3/4),
o programa transforme-o em uma melhor estrutura de dados (como as nossas
classes Expressão) e aí interprete essa árvore. É realmente um padrão de
projeto bem peculiar, e com utilização bem específica.'''
