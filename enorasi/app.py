from flask import Flask

from enorasi import party_blueprint

app = Flask(__name__)
app.register_blueprint(party_blueprint.party_bp)
