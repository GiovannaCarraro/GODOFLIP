from database.conexao import conectar

def listar_favoritos(id_usuario):
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
  
    cursor = conexao.cursor() 


    sql_verificar = "SELECT * FROM favoritos WHERE usuario_id = %s AND produto_id = %s"
    cursor.execute(sql_verificar, (id_usuario, id_produto))
    ja_existe = cursor.fetchone()

  
    if not ja_existe:
        sql_insert = "INSERT INTO favoritos (usuario_id, produto_id) VALUES (%s, %s)"
        cursor.execute(sql_insert, (id_usuario, id_produto))
        conexao.commit()
    else:

        print("Este produto já está nos favoritos do usuário.")

    cursor.close()
    conexao.close()

def remover_favorito(id_usuario, id_produto):
    conexao, cursor = conectar()
    
   
    sql = "DELETE FROM favoritos WHERE usuario_id = %s AND produto_id = %s"
    
    cursor.execute(sql, (id_usuario, id_produto))
    conexao.commit()  
    
    cursor.close()
    conexao.close()