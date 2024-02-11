from flask import Flask

from .party_blueprint import party_blueprint

app = Flask(__name__)
app.register_blueprint(party_blueprint)
