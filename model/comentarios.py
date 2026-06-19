from database.conexao import conectar

def adicionar_comentario_db(id_usuario, id_produto, texto_comentario):
    conexao, cursor = conectar()
    
    sql = "INSERT INTO comentarios (usuario_id, produto_id, comentario) VALUES (%s, %s, %s)"
    cursor.execute(sql, (id_usuario, id_produto, texto_comentario))
    
    conexao.commit() 
    
    cursor.close()
    conexao.close()

def listar_comentarios_produto(id_produto):
    conexao, cursor = conectar()
    cursor = conexao.cursor(dictionary=True)
    
    sql = """
    SELECT c.comentario, u.nome AS nome_usuario 
    FROM comentarios c
    INNER JOIN usuarios u ON c.usuario_id = u.cod_usuario
    WHERE c.produto_id = %s
    ORDER BY c.cod_comentario DESC
    """ 

    cursor.execute(sql, (id_produto,))
    comentarios = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return comentarios