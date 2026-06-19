from database.conexao import conectar


def listar_produtos():
    conexao, cursor = conectar()
    cursor = conexao.cursor(dictionary=True) 

    sql = """
    SELECT 
        p.cod_produto,
        p.nome,
        p.desc_produto,
        p.preco,
        p.categoria,
        MIN(i.url) AS url
    FROM produtos p
    INNER JOIN img_produtos i ON p.cod_produto = i.produto_id
    WHERE p.categoria = 'Skate Completo'
    GROUP BY p.cod_produto
    """

    cursor.execute(sql)
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


def achar_produto(id_produto):
    conexao, cursor = conectar()
    cursor = conexao.cursor(dictionary=True)

    # Adicionamos o INNER JOIN para puxar a url da imagem novamente
    sql = """
    SELECT 
        produtos.cod_produto,
        produtos.nome,
        produtos.desc_produto,
        produtos.preco,
        produtos.categoria,
        img_produtos.url
    FROM produtos
    INNER JOIN img_produtos
        ON produtos.cod_produto = img_produtos.produto_id
    WHERE produtos.cod_produto = %s
    """
    
    cursor.execute(sql, (id_produto,))
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    # Retorna o produto com a imagem dentro ou None se não achar
    return resultados[0] if resultados else None


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
    cursor = conexao.cursor(dictionary=True) 

    sql = """
    SELECT 
        produtos.cod_produto,
        produtos.nome,
        produtos.desc_produto,
        produtos.preco,
        produtos.categoria,
        img_produtos.url
    FROM produtos
    INNER JOIN img_produtos
        ON produtos.cod_produto = img_produtos.produto_id
    WHERE produtos.categoria = 'pecas'
    """

    cursor.execute(sql)
    pecas = cursor.fetchall() 

    cursor.close()
    conexao.close()
    
    return pecas

def listar_destaques():
    conexao, cursor = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
    SELECT 
        p.cod_produto,
        p.nome,
        p.preco,
        p.categoria,
        MIN(i.url) AS url
    FROM produtos p
    INNER JOIN img_produtos i ON p.cod_produto = i.produto_id
    GROUP BY p.cod_produto
    """

    cursor.execute(sql)
    destaques = cursor.fetchall()

    cursor.close()
    conexao.close()
    
    return destaques

def listar_acessorios():
    conexao, cursor = conectar()
    
    # Cursor como dicionário para podermos usar texto no HTML
    cursor = conexao.cursor(dictionary=True) 

    sql = """
    SELECT
        p.cod_produto,
        p.nome,
        p.desc_produto,
        p.preco,
        p.categoria,
        i.url
    FROM produtos p
    INNER JOIN img_produtos i
        ON p.cod_produto = i.produto_id
    WHERE p.categoria = 'acessorios';
    """

    cursor.execute(sql)
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos

def achar_acessorio(cod_produto):
    conexao, cursor = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
    SELECT *
    FROM produtos
    INNER JOIN img_produtos
        ON produtos.cod_produto = img_produtos.produto_id
    WHERE produtos.cod_produto = %s
    """
    
    cursor.execute(sql, (cod_produto,))
    produto = cursor.fetchone()

    cursor.close()
    conexao.close()

    return produto