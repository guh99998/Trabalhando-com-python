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
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.model.user import User
from src.db import db


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

        with Session(db) as db_session:
            try:
                user = db_session.scalar(select(User).filter_by(email=email))

                if user is None or not check_password_hash(user.password, password):
                    raise Exception('Email ou senha inválidos')

            except Exception as e:
                error = str(e)
            else:
                session['logged_user'] = user.to_json()

                return redirect(url_for('index.index'))

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
        else:
            with Session(db) as db_session:
                db_session.add(user)

                try:
                    db_session.commit()
                except IntegrityError as e:
                    error = 'Email já cadastrado'

        if error:
            flash(error, 'danger')

            return render_template('auth/register.html')
        else:
            flash('Conta criada', 'success')
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@auth_bp.get('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('index.index'))
