from flask import Blueprint, render_template, request
from minilabs.tylerminilab.lab import Marvel
tylerminilab_bp = Blueprint('tylerminilab', __name__,
                           template_folder='templates',)


@tylerminilab_bp.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("tylerminilab.html", Marvel=Marvel(int(request.form.get("series"))))
    return render_template("tylerminilab.html", Marvel=Marvel(1))

