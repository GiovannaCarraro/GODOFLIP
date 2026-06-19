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
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
    cursor.execute(sql, (email, senha))

    # Puxa tudo e limpa a linha de transmissão do banco
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    # Se achou o usuário, retorna o primeiro da lista. Se não, retorna None.
    return resultados[0] if resultados else None