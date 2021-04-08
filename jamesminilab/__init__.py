from flask import Blueprint, render_template

#
#
# IMPORTANT NOTE: My actual finished blueprints are in blueprints.py as I decided to apply my minilab to the actual project.
#
#

jamesminilab_bp = Blueprint('jamesminilab', __name__, template_folder='templates',)

@jamesminilab_bp.route('/')
def index():
    return render_template("jamesminilab.html")