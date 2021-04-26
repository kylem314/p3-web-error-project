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
    if request.form:
        all_list = []
        b = 1 # to ensure first number is 0

        newbox_counter = request.form.get('newbox_counter')
        print('number of boxes added' +str(newbox_counter))

        numberToItterate = 5 + int(newbox_counter)
        # iterating through all of the form text fields input
        for i in range(numberToItterate):
            string_used = 'user_input' + str(b)
            user_input = request.form.get(string_used)
            all_list.append(int(user_input))
            b = b + 1

        print(all_list)
        bubble = BubbleSort(all_list)
        return render_template("bubblesort.html", output_list = bubble.OuputList)
    return render_template("bubblesort.html")