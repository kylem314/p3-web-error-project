from flask import Blueprint, render_template, request
from minilabs.kyleminilab.classes import primeCheck
from minilabs.kyleminilab.bubblesort import SortAlgorithm

kyleminilab_bp = Blueprint('kyleminilab', __name__,
                           template_folder='templates',)

@kyleminilab_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("kylehomepage.html")

@kyleminilab_bp.route('/kyleminilab',methods=['GET', 'POST'])
def minilab():
    if request.method == 'POST':
        return render_template("kyleminilab.html", primeCheck = primeCheck(int(request.form.get("input"))))
    return render_template("kyleminilab.html", primeCheck = primeCheck(1))

@kyleminilab_bp.route('/kylebubblesort', methods=["GET", "POST"])
def bubblesort():
    if request.form:
        list = []
        counter = 1
        Inputs = 10
        for i in range(Inputs):
            string = 'input' + str(counter)
            input = request.form.get(string)
            list.append(int(input))
            counter += 1
        bubble = SortAlgorithm(list)
        return render_template('kylebubblesort.html', active_page='kyle', testing=bubble)
    return render_template('kylebubblesort.html', active_page='kyle')

