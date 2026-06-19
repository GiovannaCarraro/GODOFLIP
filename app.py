from flask import Flask, render_template, redirect, request, session, jsonify
from database.conexao import conectar
from model.usuario import cadastrar_usuario, verificar_login
from model.favoritos import listar_favoritos
from model.skate import listar_produtos, buscar_produto, achar_produto, listar_banners, listar_pecas, listar_destaques, listar_acessorios

app = Flask(__name__)

app.secret_key = "chiclete"

# pagina inicial 
@app.route('/')
def index():
    produtos_destaque = listar_destaques()
    return render_template('pag_inicial.html', produtos=produtos_destaque)


# pagina skates
@app.route("/skates")
def skates():

    produtos = listar_produtos()

    return render_template(
        "pag_skates.html",
        produtos=produtos
    )


@app.route("/comprar/<int:id_produto>")
def pag_comprar_skates(id_produto):

    produto = achar_produto(id_produto)

    return render_template(
        "pag_comprar_skates.html",
        produto=produto
    )

@app.route("/")
def home():
    produtos = listar_produtos()
    banners = listar_banners()

    return render_template(
        "pag_inicial.html",
        produtos=produtos,
        banners=banners, 
    )

@app.route("/pag_pecas")
def pecas():
    produtos = listar_pecas()

    return render_template(
        "pag_pecas.html",
        produtos=produtos
    )



@app.route("/pag_acessorios")
def acessorios():
    
    produtos = listar_acessorios()
    
  
    return render_template("pag_acessorios.html", produtos=produtos)

@app.route("/comprar_acessorios")
def comprar_acessorios():
    return render_template("pag_comprar_acessorios.html")

# pagina sobre nos
@app.route("/pag_sobrenos")
def sobrenos():
    return render_template("pag_sobrenos.html")
 

@app.route('/comprar_pecas/<int:id_produto>')
def comprar_pecas(id_produto):

    produto = achar_produto(id_produto)
    
    if not produto:
        abort(404)
        
    return render_template('pag_comprar_pecas.html', produto=produto)

# pagina cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']
        endereco = request.form['endereco']

        cadastrar_usuario(
            nome,
            email,
            senha,
            telefone,
            endereco
        )

        return redirect('/login')

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']

        usuario = verificar_login(email, senha)

        if usuario:
            return redirect('/')

        return "Email ou senha incorretos"

    return render_template('login.html')


@app.route('/favoritos')
def favoritos():

    usuario_id = session.get('usuario_id')

    # if not usuario_id:
    #     return redirect('/login')

    lista = listar_favoritos(usuario_id)

    favoritos = []

    for item in lista:
        favoritos.append({
            "id": item[0],
            "nome": item[1],
            "preco": item[2],
            "imagem": item[3]
        })

    return render_template(
        'pag_favoritos.html',
        favoritos=favoritos
    )


@app.route('/localizacao')
def localizacao():
    return render_template('pag_loc.html')

@app.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html')


if __name__ == "__main__":
    app.run(debug=True)