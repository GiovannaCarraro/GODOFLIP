from flask import Flask, render_template, redirect, request, session, jsonify
from database.conexao import conectar
from model.usuario import cadastrar_usuario, verificar_login
from model.favoritos import listar_favoritos

app = Flask(__name__)

# pagina inicial 
@app.route("/")
@app.route("/pagina_inicial")
def pagina_inicial():
    return render_template("pag_inicial.html")

@app.route("/skates")
def skates():
    return render_template("pag_skates.html")


@app.route("/pag_comprar")
def comprar():
    return render_template("pag_comprar_skates.html")

@app.route("/pag_acessorios")
def acessorios():
    return render_template("pag_acessorios.html")

@app.route("/pag_sobrenos")
def sobrenos():
    return render_template("pag_sobrenos.html")

@app.route("/pag_pecas")
def pecas():
    return render_template("pag_pecas.html")



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

    usuario_id = 1

    lista = listar_favoritos(usuario_id)

    favoritos = []

    for item in lista:

        favoritos.append({
            "id": item[0],
            "nome": item[1],
            "preco": item[2],
            "imagem": item[3]
        })

    return render_template('pag_favoritos.html',favoritos=favoritos)

@app.route('/localizacao')
def localizacao():
    return render_template('pag_loc.html')


if __name__ == "__main__":
    app.run(debug=True)