from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def home():
    title="Bem Vindo!!"
    linksNav=['','href=quemSomos','href=contato']
    return render_template("index.html", title=title, linksNav=linksNav)

@app.route("/home")
def index():
    title="Home"
    linksNav=['','href=quemSomos','href=contato']
    return render_template("index.html", title=title, linksNav=linksNav)

@app.route("/quemSomos")
def quemSomos():
    title="Quem Somos"
    linksNav=['href=home','','href=contato']
    return render_template("quemSomos.html", title=title, linksNav=linksNav)

@app.route("/contato")
def contato():
    title="Contato"
    linksNav=['href=home','href=/quemSomos','']
    return render_template("contato.html", title=title, linksNav=linksNav)