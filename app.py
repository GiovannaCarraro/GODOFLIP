from flask import Flask, render_template, redirect, request, session, jsonify, abort

# importa a conexão com o banco de dados
from database.conexao import conectar

# importa as funções de usuario
from model.usuario import cadastrar_usuario, verificar_login

# importa as funções de favoritos
from model.favoritos import listar_favoritos, adicionar_favorito

# importa as funções relacionadas aos produtos
from model.skate import listar_produtos, buscar_produto, achar_produto, listar_banners, listar_pecas, listar_destaques
from model.skate import listar_acessorios, achar_acessorio

# importa as funções de comentários
from model.comentarios import listar_comentarios_produto, adicionar_comentario_db
# from model.pagina import buscar_pagina_por_slug

# cria a aplicação flask
app = Flask(__name__)

# chave usada para controlar as sessões
app.secret_key = "chiclete"

# pagina inicial
@app.route("/")
def index():

    # busca os produtos em destaque
    produtos_destaque = listar_destaques()

    # busca todos os produtos
    produtos = listar_produtos()

    return render_template(
        "pag_inicial.html",
        produtos_destaque=produtos_destaque,
        produtos=produtos
    )

# pagina de skates
@app.route("/skates")
def skates():

    # busca todos os skates
    produtos = listar_produtos()

    return render_template(
        "pag_skates.html",
        produtos=produtos
    )

# pagina de peças
@app.route("/pag_pecas")
def pecas():

    # busca todas as peças
    produtos = listar_pecas()

    return render_template(
        "pag_pecas.html",
        produtos=produtos
    )

<<<<<<< HEAD
# pagina de compra das peças
@app.route('/comprar_pecas/<int:id_produto>')
def comprar_pecas(id_produto):

    # procura a peça pelo id
    produto = achar_produto(id_produto)

    # mostra erro caso não encontre
    if not produto:
        abort(404)
=======
>>>>>>> 60e35719a7035b1153b2278329d155e5633b33a5

    return render_template(
        'pag_comprar_pecas.html',
        produto=produto
    )

# pagina de acessórios
@app.route("/pag_acessorios")
def acessorios():

    # busca os acessórios
    produtos = listar_acessorios()

    return render_template(
        "pag_acessorios.html",
        produtos=produtos
    )

# pagina de compra dos acessórios
@app.route("/comprar_acessorios")
def comprar_acessorios():
    return render_template("pag_comprar_acessorios.html")

# pagina sobre nós
@app.route("/pag_sobrenos")
def sobrenos():
    return render_template("pag_sobrenos.html")

# segunda rota da pagina sobre nós
@app.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html')

# pagina de localização
@app.route('/localizacao')
def localizacao():
    return render_template('pag_loc.html')

# sistema de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    # verifica se o formulario foi enviado
    if request.method == 'POST':

        # recebe os dados digitados
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']
        endereco = request.form['endereco']

        # cadastra o usuario no banco
        cadastrar_usuario(nome, email, senha, telefone, endereco)

        return redirect('/login')

    return render_template('cadastro.html')

# sistema de login
@app.route('/login', methods=['GET', 'POST'])
def login():

    # verifica se o formulario foi enviado
    if request.method == 'POST':

        # recebe email e senha
        email = request.form['email']
        senha = request.form['senha']

        # verifica se o usuario existe
        usuario = verificar_login(email, senha)

        if usuario:

            # salva o id do usuario na sessão
            session['usuario_id'] = usuario['cod_usuario']

            return redirect('/')

        return "Email ou senha incorretos"

    return render_template('login.html')

# pagina de favoritos
@app.route('/favoritos')
def favoritos():

    # impede acesso sem login
    if 'usuario_id' not in session:
        return redirect('/login')

    # pega o id do usuario logado
    id_usuario = session['usuario_id']

    # busca os favoritos do usuario
    meus_favoritos = listar_favoritos(id_usuario)

    return render_template(
        'pag_favoritos.html',
        favoritos=meus_favoritos
    )

<<<<<<< HEAD
# adiciona um produto aos favoritos
@app.route('/adicionar_favorito', methods=['POST'])
def rota_adicionar_favorito():

    # impede acesso sem login
    if 'usuario_id' not in session:
        return redirect('/login')

    id_usuario = session['usuario_id']
    id_produto = request.form.get('produto_id')

    # adiciona o produto aos favoritos
    if id_produto:
        adicionar_favorito(id_usuario, id_produto)

    # volta para a pagina anterior
    pagina_anterior = request.referrer or '/favoritos'

    return redirect(pagina_anterior)

# sistema de comentários
@app.route("/adicionar_comentario", methods=["POST"])
def adicionar_comentario():

    # impede comentarios sem login
    if 'usuario_id' not in session:
        return redirect('/login')

    # pega os dados do comentario
    id_usuario = session['usuario_id']
    id_produto = request.form['produto_id']
    texto = request.form['texto']

    # salva o comentario no banco
    adicionar_comentario_db(id_usuario, id_produto, texto)

    return redirect(request.referrer)

# pagina de compra dos skates
@app.route("/comprar/<int:id_produto>")
def pag_comprar_skates(id_produto):

    # busca o produto selecionado
    produto = achar_produto(id_produto)

    # busca os comentarios do produto
    comentarios_do_produto = listar_comentarios_produto(id_produto)

    return render_template(
        "pag_comprar_skates.html",
        produto=produto,
        comentarios=comentarios_do_produto
    )

# inicia o servidor
=======
# Lembre-se de importar a função buscar_pagina_por_slug lá no topo!

# @app.route("/p/<slug_da_pagina>")
# def pagina_dinamica(slug_da_pagina):
#     # 1. Tenta achar a página no banco de dados usando a palavra da URL
#     pagina = buscar_pagina_por_slug(slug_da_pagina)
    
#     # 2. Se não achar nada, dá erro 404 (Página não encontrada)
#     if not pagina:
#         abort(404)
        
#     # 3. Se achar, envia os dados para o HTML genérico
#     return render_template("pagina_dinamica.html", pagina=pagina)

@app.route('/logout')
def logout():
    # Limpa todos os dados da sessão (remove o usuário fantasma)
    session.clear() 
    return redirect('/login')

>>>>>>> 60e35719a7035b1153b2278329d155e5633b33a5
if __name__ == "__main__":
    app.run(debug=True)