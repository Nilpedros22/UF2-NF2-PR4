from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/inicio")
def inicio():
    return render_template("inicio.html")


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("registro.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/quienes_somos")
def quienes_somos():
    return render_template("quienes_somos.html")


if __name__ == "__main__":
    app.run(debug=True)
