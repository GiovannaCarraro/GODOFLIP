from flask import Flask, render_template, redirect, request, session, jsonify

app = Flask(__name__)

@app.route("/")
def pagina_index():
    return render_template ("/")

# pagina inicial 
@app.route("pagina_inicial")
def pagina_inicial():
    return render_template("pag_inicial.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)