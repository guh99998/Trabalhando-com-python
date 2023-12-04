from json import JSONEncoder
from flask import Flask
import datetime

from src.controllers.auth import auth_bp
from src.controllers.index import index_bp

app = Flask(__name__)
app.secret_key = 'ad59f9fd9286a14a61f611d14c6bf2ae05da06768e84cc4d8f7a50183d3f19e1'

app.config['current_year'] = datetime.date.today().strftime("%Y")

@app.context_processor
def inject_global_variables():
    return dict(current_year=app.config['current_year'])

app.register_blueprint(index_bp)
app.register_blueprint(auth_bp)
