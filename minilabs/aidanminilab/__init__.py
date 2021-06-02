from flask import Blueprint, render_template
from flask import request
from minilabs.aidanminilab.minilab import Workouts
from minilabs.aidanminilab.bubblesort import BubbleSort

aminilab_bp = Blueprint('minilab', __name__,
                            template_folder='templates',)

@aminilab_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("minilab.html", Workouts=Workouts(int(request.form.get("series"))))
    return render_template("minilab.html", Workouts=Workouts(1))

@aminilab_bp.route('/bubblesort', methods = ['GET','POST'])
def BubbleSort():
    arr = []
    isString = False
    if request.form:
        string = request.form.get("string")
        arr = string.split()
        input = string.split()
        if(request.form["select"] == "string"):
            try:
                isString = True
                return render_template("bubblesort.html",sorted_list = BubbleSort(arr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("bubblesort.html",sorted_list = "Can Only Contain A String",input_list = "Error")
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