from database.conexao import conectar


def cadastrar_usuario(nome, email, senha, telefone, endereco):

    conexao, cursor = conectar()

    sql = """
    INSERT INTO usuarios
    (nome, email, senha, telefone, endereco)
    VALUES (%s,%s,%s,%s,%s)
    """

    valores = (
        nome,
        email,
        senha,
        telefone,
        endereco
    )

    cursor.execute(sql, valores)

    conexao.commit()

    cursor.close()
    conexao.close()


def verificar_login(email, senha):

    conexao, cursor = conectar()

    sql = """
    SELECT *
    FROM usuarios
    WHERE email = %s
    AND senha = %s
    """

    cursor.execute(sql, (email, senha))

    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario