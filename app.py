from flask import Flask, render_template, redirect, request, session, jsonify, abort
from model.usuario import cadastrar_usuario, verificar_login
from model.favoritos import listar_favoritos, adicionar_favorito, remover_favorito
from model.skate import listar_produtos, buscar_produto, achar_produto, listar_banners, listar_pecas, listar_destaques
from model.skate import listar_acessorios, achar_acessorio
from model.comentarios import listar_comentarios_produto, adicionar_comentario_db

# from model.pagina import buscar_pagina_por_slug

app = Flask(__name__)
app.secret_key = "chiclete"


@app.route("/")
def index():
    produtos_destaque = listar_destaques()
    produtos = listar_produtos()
    return render_template(
        "pag_inicial.html",
        produtos_destaque=produtos_destaque,
        produtos=produtos
    )

# 2. PAGINA SKATES
@app.route("/skates")
def skates():
    produtos = listar_produtos()
    return render_template(
        "pag_skates.html",
        produtos=produtos
    )

# 3. PAGINA PECAS
@app.route("/pag_pecas")
def pecas():
    produtos = listar_pecas()
    return render_template(
        "pag_pecas.html",
        produtos=produtos
    )


# 5. PAGINA ACESSORIOS
@app.route("/pag_acessorios")
def acessorios():
    produtos = listar_acessorios()
    return render_template("pag_acessorios.html", produtos=produtos)

# 4. COMPRAR PECAS
@app.route('/comprar_pecas/<int:id_produto>')
def comprar_pecas(id_produto):
    produto = achar_produto(id_produto)
    if not produto:
        abort(404)
        
    # BUSCA OS COMENTÁRIOS DA PEÇA
    comentarios_da_peca = listar_comentarios_produto(id_produto)
        
    return render_template(
        'pag_comprar_pecas.html', 
        produto=produto, 
        comentarios=comentarios_da_peca # Passa para o HTML
    )

# 5. COMPRAR ACESSORIOS 
# (Nota: Ajustei sua rota para receber o id_produto, igual às outras!)
@app.route("/comprar_acessorios/<int:id_produto>")
def comprar_acessorios(id_produto):
    produto = achar_acessorio(id_produto) # Usa a sua função que busca acessório
    if not produto:
        abort(404)

    # BUSCA OS COMENTÁRIOS DO ACESSÓRIO
    comentarios_do_acessorio = listar_comentarios_produto(id_produto)

    return render_template(
        "pag_comprar_acessorios.html", 
        produto=produto, 
        comentarios=comentarios_do_acessorio # Passa para o HTML
    )


@app.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html')

# 7. LOCALIZACAO
@app.route('/localizacao')
def localizacao():
    return render_template('pag_loc.html')

# 8. SISTEMA DE CADASTRO E LOGIN
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
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        # Aqui entra a sua lógica de checar o login no banco...
        return redirect('/')
        
    # Se o método for GET, apenas renderiza a página de login
    return render_template('login.html')

# 9. SISTEMA DE FAVORITOS
@app.route('/favoritos')
def favoritos(): 
    if 'usuario_id' not in session:
        return redirect('/login') 
        
    id_usuario = session['usuario_id']
    meus_favoritos = listar_favoritos(id_usuario)
    return render_template('pag_favoritos.html', favoritos=meus_favoritos)

@app.route('/adicionar_favorito', methods=['POST'])
def rota_adicionar_favorito():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    id_usuario = session['usuario_id']
    id_produto = request.form.get('produto_id')
    
    if id_produto:
        adicionar_favorito(id_usuario, id_produto)
    
    pagina_anterior = request.referrer or '/favoritos'
    return redirect(pagina_anterior)

# 10. SISTEMA DE COMENTARIOS
@app.route("/adicionar_comentario", methods=["POST"])
def adicionar_comentario():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    id_usuario = session['usuario_id']
    id_produto = request.form['produto_id']
    texto = request.form['texto'] 
    
    adicionar_comentario_db(id_usuario, id_produto, texto)
    return redirect(request.referrer)

# 11. PAGINA DE COMPRA DO SKATE (Única, com os comentários inclusos)
@app.route("/comprar/<int:id_produto>") 
def pag_comprar_skates(id_produto):
    produto = achar_produto(id_produto) 
    comentarios_do_produto = listar_comentarios_produto(id_produto)
    
    return render_template(
        "pag_comprar_skates.html", 
        produto=produto, 
        comentarios=comentarios_do_produto 
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

if __name__ == "__main__":
    app.run(debug=True)