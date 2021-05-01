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

    # conversion = Conversion('', all_list)
    # return render_template("colin/conversion.html", user_input=user_input, conversion=conversion,
    # list_conversion=conversion._list ,active_page='colin', type='multi', type_js=json.dumps('multi'))

    return render_template("bubblesort.html", active_page='calvin')