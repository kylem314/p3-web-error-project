from flask import Blueprint, render_template
from flask import request
from minilabs.kyleminilab import classes

kyleminilab_bp = Blueprint('kyleminilab', __name__,
                            template_folder='templates',)

@kyleminilab_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("kyleminilab.html", Workouts=Workouts(int(request.form.get("series"))))
    return render_template("kyleminilab.html", Workouts=Workouts(1))