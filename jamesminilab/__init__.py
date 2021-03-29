from flask import Blueprint, render_template

jamesminilab_bp = Blueprint('jamesminilab', __name__, template_folder='templates',)

@jamesminilab_bp.route('/')
def index():
    return render_template("jamesminilab.html")