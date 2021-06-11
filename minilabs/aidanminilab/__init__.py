from flask import Blueprint, render_template
from flask import request
from .algo.minilab import Workouts
from .algo.bubblesort import BubbleSort

"""aminilab_bp = Blueprint('aminilab', __name__,
                        template_folder='templates',)"""

aminilab_bp = Blueprint('aminilab_bp', __name__, template_folder='templates', static_folder='static', static_url_path='assets')

@aminilab_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("aidanminilab.html", Workouts=Workouts(int(request.form.get("series"))))
    return render_template("aidanminilab.html", Workouts=Workouts(1))

@aminilab_bp.route('/bubblesort', methods = ['GET','POST'])
def bubbleSort():
    arr = []
    isString = False
    if request.form:
        string = request.form.get("string")
        arr = string.split()
        input = string.split()
        # check if inputted values are string
        if(request.form["select"] == "string"):
            #if string then sort strings
            try:
                isString = True
                return render_template("bubblesort.html",sorted_list = BubbleSort(arr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("bubblesort.html",sorted_list = "Can Only Contain A String",input_list = "Error")
        #if not string then sort for integers
        else:
            try:
                for j in range (0,len(arr)):
                    arr[j] = int(arr[j])
                for j in range (0,len(input)):
                    input[j] = int(input[j])
                return render_template("bubblesort.html",sorted_list = BubbleSort(arr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("bubblesort.html",sorted_list = "Can Only Contain An Integer",input_list = "Error")

    return render_template("bubblesort.html",sorted_list = BubbleSort(arr,isString).OutputList,input_list = arr)