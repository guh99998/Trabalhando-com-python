from flask import Flask, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)

# @app.route('/')
# def home():
#     return '<h1>Olá, bem vindo</h1>'
#o código foi colocado na rota raíz, então assim que entrarmos no endereço do servidor, a mensagem irá aparecer

# @app.route('/pessoa/<string: nome>')
# def ola(nome):
#     return f'<h1>Bem vindo, {escape(nome)}</h1>'
#trabalhando com parâmetros, indo até a nova rota com parâmetros, no parâmetro também podemos definir o tipo
#o escape é utilizado para o parâmetro passado ficar seguro

@app.route('/')
@app.route('/<nome>')
def index(nome=None):
    return render_template('index.html', nome=nome)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['email'] == 'gustavo@gmail.com' and request.form['senha'] == '123':

            email = request.form['email']

            return render_template('home.html', email=email)
        else:
            error = 'Login inválido'

    return render_template('login.html', error=error)

