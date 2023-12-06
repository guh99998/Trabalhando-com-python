from flask import (
    Blueprint,
    render_template,
    session
)

index_bp = Blueprint('index', __name__, url_prefix='/', template_folder='templates')

@index_bp.get('/')
def index():
    user = session.get('logged_user')

    return render_template('index.html', user=user)
