from flask import Blueprint, render_template, request
from minilabs.tylerminilab.lab import Marvel
from minilabs.tylerminilab.bubblesort import BubbleSort

tylerminilab_bp = Blueprint('tylerminilab', __name__,
                           template_folder='templates',)

#route to homepage
@tylerminilab_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("tylerhomepage.html")

#route for minilab
@tylerminilab_bp.route('/tylerminilab',methods=['GET', 'POST'])
def minilab():
    if request.method == 'POST':
        return render_template("tylerminilab.html", Marvel=Marvel(int(request.form.get("series"))))
    return render_template("tylerminilab.html", Marvel=Marvel(1))

#bubble sort mini lab
@tylerminilab_bp.route('/tylerbubblesort', methods=["GET", "POST"])
def bubblesort():
    if request.form:
        list = []
        b = 1
        Numbers = 5
        for i in range(Numbers):
            string = 'input' + str(b)
            input = request.form.get(string)
            list.append(int(input))
            b = b + 1
        bubble=BubbleSort(list)
        return render_template('tylerbubblesort.html', active_page='tyler', testing=bubble)
    return render_template('tylerbubblesort.html', active_page='tyler')

