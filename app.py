from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    # Os dados são recebidos apenas para a simulação.
    # Não são armazenados em banco de dados.
    nome = request.form.get("nome")

    return render_template(
        "conscientizacao.html",
        nome=nome
    )


if __name__ == "__main__":
    app.run(debug=True)