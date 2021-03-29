from flask import Blueprint, render_template
kyleminilab_bp = Blueprint('kyleminilab', __name__,
                           template_folder='templates',)
@kyleminilab_bp.route('/')
def index():
    return render_template("kyleminilab.html")