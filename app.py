from flask import Flask, render_template, redirect, request, session, jsonify

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template ("/")
