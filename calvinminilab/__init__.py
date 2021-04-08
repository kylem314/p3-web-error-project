from flask import Blueprint, render_template, request
from calvinminilab.lab import Meat

tylerminilab_bp = Blueprint('tylerminilab', __name__,
                            template_folder='templates',)


@calvinminilab_bp.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("calvinminilab.html", Meat =Meat(int(request.form.get("series"))))
    return render_template("calvinminilab.html", Meat=Meat(1))