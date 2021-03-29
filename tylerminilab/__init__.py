from flask import Blueprint, render_template
tylerminilab_bp = Blueprint('tylerminilab', __name__,
                           template_folder='templates',)

@tylerminilab_bp.route('/')
def index():
    return render_template("tylerminilab.html")