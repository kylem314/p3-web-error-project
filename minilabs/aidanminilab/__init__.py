from flask import Blueprint, render_template
from flask import request
from minilabs.aidanminilab.minilab import Workouts

aidanminilab_bp = Blueprint('aidanminilab', __name__,
                            template_folder='templates',)

@aidanminilab_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("aidanminilab.html", Workouts=Workouts(int(request.form.get("series"))))
    return render_template("aidanminilab.html", Workouts=Workouts(1))