from flask import Blueprint, render_template

aidanminilab_bp = Blueprint('aidanminilab', __name__,
                            template_folder='templates',)

@aidanminilab_bp.route('/')
def index():
    return render_template("aidanminilab.html")