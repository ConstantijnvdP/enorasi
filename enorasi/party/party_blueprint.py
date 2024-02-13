from pathlib import Path
from flask import Blueprint, render_template

party_bp = Blueprint('party_blueprint', __name__,
                    template_folder="templates",
                    static_folder='static',
                    static_url_path='assets')

party_data = {
    "Gaulius": {"hp": 55,
                "max_hp": 75,
                "status": "RAGE!",
                "img": "genasi.jpg"
               },
    "Kezneya": {"hp": 60,
                "max_hp": 60,
                "status": "Hidden",
                "img": "genasi.jpg"
               },
    "Gilliam": {"hp": 8,
                "max_hp": 72,
                "status": "None",
                "img": "genasi.jpg"
               }
}

@party_bp.route('/')
def index():
    return render_template("party/party_hp.html", party_data=party_data)
