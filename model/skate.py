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


def buscar_produto(cod_produto):
    conexao, cursor = conectar()

    cursor.execute(
        """
        SELECT *
        FROM produtos
        WHERE cod_produto = %s
        """,
        (cod_produto,)
    )

    produto = cursor.fetchone()

    cursor.close()
    conexao.close()

    return produto