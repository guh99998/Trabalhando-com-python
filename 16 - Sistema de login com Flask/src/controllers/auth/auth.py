import functools
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from werkzeug.security import check_password_hash
from src.model.user import User


users: list[User] = []

auth_bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('logged_user') is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

def logout_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('logged_user'):
            return redirect(url_for('index.index'))

        return view(**kwargs)

    return wrapped_view

@auth_bp.route('/login', methods=('GET', 'POST'))
@logout_required
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        error = None

        for user in users:
            if user.email == email and check_password_hash(user.password, password):
                session['logged_user'] = user.to_json()

                return redirect(url_for('index.index'))
        else:
            error = 'Email ou senha inválidos'

        flash(error, 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/register', methods=('GET', 'POST'))
@logout_required
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        error = None

        try:
            user = User(name=name, email=email, password=password)
        except Exception as e:
            error = str(e)

            flash(error, 'danger')

            return render_template('auth/register.html')
        else:
            users.append(user)
            flash('Conta criada', 'success')
            print()
            print()
            print()
            print(users)
            print()
            print()
            print()
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')
@auth_bp.get('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('index.index'))
