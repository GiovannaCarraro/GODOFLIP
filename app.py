from flask import Flask, render_template, redirect, request, session, jsonify, abort
from database.conexao import conectar
from model.usuario import cadastrar_usuario, verificar_login
from model.favoritos import listar_favoritos, adicionar_favorito
from model.skate import listar_produtos, buscar_produto, achar_produto, listar_banners, listar_pecas, listar_destaques
from model.skate import listar_acessorios, achar_acessorio
from model.comentarios import listar_comentarios_produto, adicionar_comentario_db

app = Flask(__name__)
app.secret_key = "chiclete"

# 1. PAGINA INICIAL (Resolvido o clone que tinha aqui)
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

# 4. COMPRAR PECAS
@app.route('/comprar_pecas/<int:id_produto>')
def comprar_pecas(id_produto):
    produto = achar_produto(id_produto)
    if not produto:
        abort(404)
    return render_template('pag_comprar_pecas.html', produto=produto)

# 5. PAGINA ACESSORIOS
@app.route("/pag_acessorios")
def acessorios():
    produtos = listar_acessorios()
    return render_template("pag_acessorios.html", produtos=produtos)

@app.route("/comprar_acessorios")
def comprar_acessorios():
    return render_template("pag_comprar_acessorios.html")

# 6. PAGINA SOBRE NOS
@app.route("/pag_sobrenos")
def sobrenos():
    return render_template("pag_sobrenos.html")

@app.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html')

# 7. LOCALIZACAO
@app.route('/localizacao')
def localizacao():
    return render_template('pag_loc.html')

# 8. SISTEMA DE CADASTRO E LOGIN
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']
        endereco = request.form['endereco']

        cadastrar_usuario(nome, email, senha, telefone, endereco)
        return redirect('/login')

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = verificar_login(email, senha)

        if usuario:
            session['usuario_id'] = usuario['cod_usuario'] 
            return redirect('/')

        return "Email ou senha incorretos"

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
<<<<<<< HEAD

@app.route('/localizacao')
def localizacao():
    return render_template('pag_loc.html')
=======
>>>>>>> f2676499b588b5dcf3ad1ccc46c06c5a3706edd4

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

if __name__ == "__main__":
    app.run(debug=True)