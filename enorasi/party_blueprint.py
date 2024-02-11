from flask import Blueprint

party_blueprint = Blueprint('party_blueprint', __name__)

@party_blueprint.route('/')
def index():
    return "Party info here"
