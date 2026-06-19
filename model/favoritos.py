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
    # Usamos o cursor normal aqui para essa verificação rápida
    cursor = conexao.cursor() 

    # 1. Pergunta para o banco se esse usuário já favoritou esse produto específico
    sql_verificar = "SELECT * FROM favoritos WHERE usuario_id = %s AND produto_id = %s"
    cursor.execute(sql_verificar, (id_usuario, id_produto))
    ja_existe = cursor.fetchone()

    # 2. Se o banco disser "não encontrei nada" (None), aí sim a gente faz o INSERT
    if not ja_existe:
        sql_insert = "INSERT INTO favoritos (usuario_id, produto_id) VALUES (%s, %s)"
        cursor.execute(sql_insert, (id_usuario, id_produto))
        conexao.commit()
    else:
        # Se já existir, o Python ignora silenciosamente e não duplica nada!
        print("Este produto já está nos favoritos do usuário.")

    cursor.close()
    conexao.close()