from database.conexao import conectar

def listar_favoritos(id_usuario):
    conexao, cursor = conectar()
    cursor = conexao.cursor(dictionary=True)

    # O segredo está no MIN(i.url) e no GROUP BY no final
    sql = """
    SELECT 
        p.cod_produto,
        p.nome,
        p.preco,
        p.categoria,
        MIN(i.url) AS url
    FROM favoritos f
    INNER JOIN produtos p ON f.produto_id = p.cod_produto
    INNER JOIN img_produtos i ON p.cod_produto = i.produto_id
    WHERE f.usuario_id = %s
    GROUP BY p.cod_produto
    """
    
    cursor.execute(sql, (id_usuario,))
    favoritos = cursor.fetchall()

    cursor.close()
    conexao.close()
    
    return favoritos

def adicionar_favorito(id_usuario, id_produto):
    conexao, cursor = conectar()
    
    sql = "INSERT INTO favoritos (usuario_id, produto_id) VALUES (%s, %s)"
    cursor.execute(sql, (id_usuario, id_produto))
    
    # SE FALTAR ESSA LINHA, O BANCO NÃO SALVA! 🔴
    conexao.commit() 
    
    cursor.close()
    conexao.close()