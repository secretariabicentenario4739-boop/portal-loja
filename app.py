from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "segredo_loja"

def conectar():
    return sqlite3.connect("database.db")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/entrar", methods=["POST"])
def entrar():
    email = request.form["email"]
    senha = request.form["senha"]

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
    usuario = cursor.fetchone()

    conn.close()

    if usuario:
        session["usuario"] = usuario[1]
        return redirect("/dashboard")

    return "Login inválido"

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect("/")
    return render_template("dashboard.html", usuario=session["usuario"])

@app.route("/atas")
def atas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM atas ORDER BY data DESC")
    atas = cursor.fetchall()

    conn.close()

    return render_template("atas.html", atas=atas)

app.run(debug=True)