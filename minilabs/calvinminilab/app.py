from flask import request, render_template
from minilabs.calvinminilab.minilab import Meat
from minilabs.calvinminilab.bubblesort import BubbleSort
from minilabs.calvinminilab import calvinminilab_bp




@calvinminilab_bp.route('/',methods = ["GET","POST"])
def index():
    return render_template("landingpage.html")

@calvinminilab_bp.route('/meatgrinder',methods=['GET', 'POST'])
def meatgrinder():
    if request.method == 'POST':
        return render_template("calvinminilab.html", Meat =Meat(int(request.form.get("series"))))
    return render_template("calvinminilab.html", Meat=Meat(1))

@calvinminilab_bp.route('/bubbleSort',methods = ["GET","POST"])
def bubbleSort():
    arr = []
    isString = False
    if request.form:
        string = request.form.get("string")
        arr = string.split()
        original = string.split()
        if(request.form["select"] == "integer"):
            try:
                for j in range (0,len(arr)):
                    arr[j] = int(arr[j])
                for j in range (0,len(original)):
                    original[j] = int(original[j])
                return render_template("bubblesort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = original)
            except ValueError:
                return render_template("bubblesort.html",output_list = "Can Only Contain String or Integer",original_list = "Error")
        else:
            try:
                isString = True
                return render_template("bubblesort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = original)
            except ValueError:
                return render_template("bubblesort.html",output_list = "Can Only Contain String or Integer",original_list = "Error")
    return render_template("bubblesort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = arr)
