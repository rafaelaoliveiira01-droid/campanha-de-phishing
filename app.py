from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def cadastro():
    return render_template("cadastro.html")


@app.route("/informacoes", methods=["POST"])
def informacoes():
    nome = request.form.get("nome")

    return render_template(
        "informacoes.html",
        nome=nome
    )


if __name__ == "__main__":
    app.run(debug=True)