from flask import Flask, render_template, redirect, request, session, jsonify

app = Flask(__name__)

# pagina inicial 
@app.route("/")
@app.route("/pagina_inicial")
def pagina_inicial():
    return render_template("pag_inicial.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)