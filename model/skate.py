from database.conexao import conectar


def listar_produtos():
    conexao, cursor = conectar()

    cursor.execute("""
        SELECT * FROM produtos
            inner join img_produtos on produto_id = cod_produto
    """)

    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos