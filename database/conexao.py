import mysql.connector


def conectar():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_skate"
    )

    cursor = conexao.cursor()

    return conexao, cursor