from flask import Flask
import datetime
from .controllers import blueprints
from .db import init_db

app = Flask(__name__)
app.secret_key = 'ad59f9fd9286a14a61f611d14c6bf2ae05da06768e84cc4d8f7a50183d3f19e1'

@app.context_processor
def inject_global_variables():
    return dict(current_year=datetime.date.today().strftime("%Y"))

for blueprint in blueprints:
    app.register_blueprint(blueprint)

init_db()
