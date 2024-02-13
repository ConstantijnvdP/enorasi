from flask import Flask

from enorasi.party import party_blueprint

app = Flask(__name__)
app.register_blueprint(party_blueprint.party_bp, url_prefix='/party')
