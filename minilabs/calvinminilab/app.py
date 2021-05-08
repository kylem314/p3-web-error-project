from flask import request, render_template
from minilabs.calvinminilab.algo.minilab import Meat
from minilabs.calvinminilab.algo.bubblesort import BubbleSort
from minilabs.calvinminilab import calvinminilab_bp


@calvinminilab_bp.route('/',methods = ["GET","POST"])
def index():
    return render_template("landingpage.html")

@calvinminilab_bp.route('/meatgrinder',methods=['GET', 'POST'])
def meatgrinder():
    if request.method == 'POST':
        return render_template("meat.html", Meat =Meat(int(request.form.get("series"))))
    return render_template("meat.html", Meat=Meat(1))

@calvinminilab_bp.route('/bubblesort', methods=["GET", "POST"])
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
        return render_template('calvinbubblesort.html', active_page='calvin', testing=bubble)
    return render_template('calvinbubblesort.html', active_page='calvin')
