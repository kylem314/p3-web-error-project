from flask import Blueprint, render_template
from flask import request
from calvinminilab.minilab import Meat

calvinminilab_bp = Blueprint('calvinminilab', __name__,
                            template_folder='templates',)


@calvinminilab_bp.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("calvinminilab.html", Meat =Meat(int(request.form.get("series"))))
    return render_template("calvinminilab.html", Meat=Meat(1))