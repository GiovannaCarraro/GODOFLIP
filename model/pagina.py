from database.conexao import conectar

def buscar_pagina_por_slug(slug_da_pagina):
    conexao, cursor = conectar()
    cursor = conexao.cursor(dictionary=True)
    
    sql = "SELECT * FROM paginas_dinamicas WHERE slug = %s"
    cursor.execute(sql, (slug_da_pagina,))
    pagina = cursor.fetchone()
    
    cursor.close()
    conexao.close()
    
    return pagina