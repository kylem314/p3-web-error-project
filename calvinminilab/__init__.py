
from flask import Blueprint, render_template
calvinminilab_bp = Blueprint('calvinminilab', __name__, template_folder='templates',)

@calvinminilab_bp.route('/')
def index():
    return render_template("calvinminilab.html")