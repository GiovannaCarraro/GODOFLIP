from database.conexao import conectar


def listar_produtos():
    conexao, cursor = conectar()

    cursor.execute("""
        SELECT *
        FROM produtos
    """)

    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos