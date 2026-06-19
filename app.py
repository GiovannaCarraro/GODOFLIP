from flask import Flask, render_template, redirect, request, session, jsonify, abort
from database.conexao import conectar
from model.usuario import cadastrar_usuario, verificar_login

from model.favoritos import listar_favoritos, adicionar_favorito


from model.skate import listar_produtos, buscar_produto, achar_produto, listar_banners, listar_pecas, listar_destaques
from model.skate import listar_acessorios, achar_acessorio

app = Flask(__name__)

app.secret_key = "chiclete"

@app.route("/")
def index():
    produtos_destaque = listar_destaques()
    produtos = listar_produtos()

    # Removemos o listar_banners() e a variável banners do render_template
    return render_template(
        "pag_inicial.html",
        produtos_destaque=produtos_destaque,
        produtos=produtos
    )
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
          
            session['usuario_id'] = usuario['cod_usuario'] 
            
            return redirect('/')

        return "Email ou senha incorretos"

    return render_template('login.html')


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
@app.route('/localizacao')
def localizacao():
    return render_template('pag_loc.html')

@app.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html')


if __name__ == "__main__":
    app.run(debug=True)