from flask import Flask, render_template, redirect, request, session, jsonify, abort

# importa a conexão com o banco de dados
from database.conexao import conectar

# importa as funções de usuario
from model.usuario import cadastrar_usuario, verificar_login
from model.favoritos import listar_favoritos, adicionar_favorito, remover_favorito
from model.skate import listar_produtos, buscar_produto, achar_produto, listar_banners, listar_pecas, listar_destaques
from model.skate import listar_acessorios, achar_acessorio

# importa as funções de comentários
from model.comentarios import listar_comentarios_produto, adicionar_comentario_db

# from model.pagina import buscar_pagina_por_slug

# cria a aplicação flask
app = Flask(__name__)

# chave usada para controlar as sessões
app.secret_key = "chiclete"

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

# pagina de compra das peças
@app.route('/comprar_pecas/<int:id_produto>')
def comprar_pecas(id_produto):

    # procura a peça pelo id
    produto = achar_produto(id_produto)

    # mostra erro caso não encontre
    if not produto:
        abort(404)

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
def rota_cadastro():
    print(f"Recebi uma requisição com o método: {request.method}") # Isso vai aparecer no seu terminal!
    
    if request.method == 'POST':
        # Pegando os dados do formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        print(f"Tentativa de cadastro: Nome={nome}, Email={email}")
        
        # Por enquanto, apenas redireciona para o login para testar a rota
        return redirect('/login')

    # Se for GET, renderiza o HTML correspondente
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    # verifica se o formulario foi enviado
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        # Aqui entra a sua lógica de checar o login no banco...
        return redirect('/')
        
    # Se o método for GET, apenas renderiza a página de login
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

@app.route('/remover_favorito', methods=['POST'])
def rota_remover_favorito():
    # Se o usuário não estiver logado, manda para o login
    if 'usuario_id' not in session:
        return redirect('/login')
    
    id_usuario = session['usuario_id']
    id_produto = request.form.get('produto_id')
    
    if id_produto:
        # Chama a função que criamos no model para deletar do banco
        remover_favorito(id_usuario, id_produto)
        
    # Atualiza a própria página de favoritos para mostrar que sumiu
    return redirect('/favoritos')

# Lembre-se de importar a função buscar_pagina_por_slug lá no topo!

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
if __name__ == "__main__":
    app.run(debug=True)