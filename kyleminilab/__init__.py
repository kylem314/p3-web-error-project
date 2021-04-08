from flask import Blueprint, render_template
from flask import request
from kyleminilab.classes import primeCheck

kyleminilab_bp = Blueprint('kyleminilab', __name__,
                            template_folder='templates',)

@kyleminilab_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("kyleminilab.html", Primes=primeCheck(int(request.form.get("input"))))
    return render_template("kyleminilab.html", Primes=primeCheck(1))