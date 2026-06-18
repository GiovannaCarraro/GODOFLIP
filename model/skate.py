from database.conexao import conectar


def listar_produtos():
    conexao, cursor = conectar()

    cursor.execute("""
        SELECT *
        FROM produtos
        INNER JOIN img_produtos
        ON produtos.cod_produto = img_produtos.produto_id
        WHERE produtos.categoria = 'Skate Completo';
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


def achar_produto(cod_produto):
    conexao, cursor = conectar()

    cursor.execute("""
        SELECT *
        FROM produtos
        INNER JOIN img_produtos
            ON produtos.cod_produto = img_produtos.produto_id
        WHERE produtos.cod_produto = %s
    """, (cod_produto,))

    produto = cursor.fetchone()

    cursor.close()
    conexao.close()

    return produto


def listar_banners():
    conexao, cursor = conectar()

    cursor.execute("""
        SELECT *
        FROM banner
    """)

    banners = cursor.fetchall()

    cursor.close()
    conexao.close()

    return banners


def listar_pecas():
    conexao, cursor = conectar()

    sql = """
    SELECT
    p.cod_produto,
    p.nome,
    p.categoria,
    i.url
FROM produtos p
INNER JOIN img_produtos i
ON p.cod_produto = i.produto_id
WHERE p.categoria = 'pecas';
    """

    cursor.execute(sql)
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos

def listar_destaques():
    conexao, cursor = conectar()

    # Busca 4 produtos aleatórios que tenham imagem
    sql = """
    SELECT 
        p.cod_produto, 
        p.nome, 
        p.preco, 
        i.url 
    FROM produtos p
    INNER JOIN img_produtos i ON p.cod_produto = i.produto_id
    ORDER BY RAND()
    LIMIT 4;
    """

    cursor.execute(sql)
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos