from connection_factory import get_connection

# . Cria uma conexão com o banco usando Padrão Factory
connection = get_connection()

tab_cursos = connection.cursos()

# executa a query
tab_cursos.execute('SELECT * from cursos')

# itera sobre o resultado
for linha in tab_cursos:
    print(linha)

# fecha a conexão
connection.close()

# ! Factory Vs Builder
'''No primeiro curso, tínhamos também um exemplo de um objeto que é difícil de
ser criado. Demos o exemplo da classe NotaFiscal. Lá, uma nota fiscal era
composta por nome da pessoa, ítens da nota, valor e etc. Tudo isso tornava o
objeto difícil de ser criado e utilizamos recursos do Python que nos ajudou
bastante neste processo de criação. Também vimos como aplicar o padrão Builder
na íntegra para resolver o mesmo problema de criação de objetos. Mas qual a
diferença entre Factory e Builder, já que o Factory também ajuda na construção?
No Builder, ainda estamos no controle da criação do objeto, porém com o auxílio
do Builder e podemos construir um objetos de diferentes maneiras. Já o Factory,
não participamos do processo de criação do objeto, isto é, já recebemos o
objeto pronto!

Ambos são padrões de projeto que visam resolver problemas de criação de
objetos. O que muda de um pro outro é basicamente a semântica. Geralmente
usamos um builder quando precisamos passar diversas informações para a lógica
que monta o objeto. No caso da Nota Fiscal, passamos nome, ítens, etc. Usamos
uma fábrica quando temos que isolar o processo de criação de um objeto em um
único lugar. Essa fábrica pode descobrir como criar o objeto dentro dela
própria, mas geralmente ela não precisa de muitas informações para criar o
objeto.
Ref: Alura: https://cursos.alura.com.br/course/design-patterns-python-2'''
