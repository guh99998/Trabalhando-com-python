from flask import Flask, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/<nome>')
def index(nome=None):
    return render_template('index.html', nome=nome)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'Método POST'
#     else:
#         return 'Método GET'

# @app.get('/login')
# def login_get():
#     return 'Método GET'

# @app.post('/login')
# def login_post():
#     return 'Método POST'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['email'] == 'alberto@gmail.com' and request.form['senha'] == '123':

            email = request.form['email']

            return render_template('home.html', email=email)
        else:
            error = 'Login inválido'

    return render_template('login.html', error=error)

@app.route('/user/<string:nome>')
def profile(nome):
    return f'<h1>Essa conta é do/a {escape(nome)}</h1>'

@app.route('/user/<int:id>')
def profile_by_id(id):
    return f'<h1>Essa conta é do usuário {escape(id)}</h1>'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('profile', nome='John Doe'))

# with app.test_request_context():
#     print()
#     print(url_for('static', filename='style.css'))
#     print()

with app.test_request_context('/hello', method='POST'):
    print(request.path)
    print(request.method)