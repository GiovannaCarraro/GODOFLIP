from database.conexao import conectar
def listar_favoritos(usuario_id):

    conexao, cursor = conectar()

    sql = """
    SELECT
        p.cod_produto,
        p.nome,
        p.preco,
        i.url
    FROM favoritos f
    INNER JOIN produtos p
        ON f.produto_id = p.cod_produto
    INNER JOIN img_produtos i
        ON p.cod_produto = i.produto_id
    WHERE f.usuario_id = %s
    """

    cursor.execute(sql, (usuario_id,))

    favoritos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return favoritos

