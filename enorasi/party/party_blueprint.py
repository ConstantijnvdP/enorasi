from flask import Blueprint, render_template

party_bp = Blueprint('party_blueprint', __name__,
                    template_folder="templates")

party_data = {
    "gaulius": {"hp": 55,
                "max_hp": 75,
                "status": "RAGE!"
               },
    "kezneya": {"hp": 60,
                "max_hp": 60,
                "status": "Hidden"
               },
    "Gilliam": {"hp": 8,
                "max_hp": 72,
                "status": "None"
               }
}

@party_bp.route('/')
def index():
    return render_template("party/party_hp.html", party_data=party_data)
