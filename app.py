from flask import Flask, render_template, redirect, request, session, jsonify
from model.usuario import cadastrar_usuario, verificar_login

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template ("/")

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
