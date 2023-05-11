from flask import Flask, render_template, request, url_for, jsonify

from flask_mysqldb import MySQL

app = Flask("__name__")
# conexão com o banco de dados
app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'senhaDoROOT'
app.config['MYSQL_DB'] = 'UNES'

mysql = MySQL(app)

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

@app.route("/contato", methods=['GET', 'POST'])
def contato():
    d='none'
    title="Contato"
    linksNav=['href=home','href=/quemSomos','']
    if request.method == "POST":
        ema = request.form['email']
        ass = request.form['assunto']
        des = request.form['descrição']
        cur = mysql.connection.cursor()
        cur.execute(f'INSERT INTO Contato(email_contato, assunto_contato, descricao_contato) VALUES ("{ema}", "{ass}", "{des}")')
        mysql.connection.commit()
        cur.close()
        d='block'
        return render_template("contato.html", title=title, linksNav=linksNav, d=d)
    return render_template("contato.html", title=title, linksNav=linksNav, d=d)