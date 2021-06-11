import MySQLdb


def get_connection():
    connection = MySQLdb.connect(
        host="localhost",
        user='root',
        passwd='',
        db='alura')
    return connection


# ! Nomenclatura
'''Costuma-se usar o sufixo Factory nas nossas classes que são fábricas.'''
