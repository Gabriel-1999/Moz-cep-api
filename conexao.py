import sqlite3 as sql


def create_database():
    conexao = sql.connect("cep.db", check_same_thread=False)
    cur = conexao.cursor()
    return conexao, cur
