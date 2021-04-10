from flask import Flask, render_template, url_for, request, redirect
from aidanminilab import aidanminilab_bp
from calvinminilab import calvinminilab_bp
from blueprints import Blueprints



app = Flask(__name__)
app.register_blueprint(aidanminilab_bp, url_prefix='/aidanminilab')
app.register_blueprint(calvinminilab_bp, url_prefix='/calvinminilab')

#def margindef():
#    marginx=0
 #   return marginx


#margindef()

marginx=0

marginbattleshipx=0
marginbattleshiptop=0



print(marginx)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/otherpage')
def otherpage():
    return render_template('otherpage.html', test='Select A Square')

#404 page
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', body_class = 'page_404' ), 404

@app.route('/movingimage')
def movingimage():
    global marginx
    marginx = 0

    return render_template('MovingImage.html')

@app.route('/boatright')
def boatright():
    global marginx
    marginx += 25
    if marginx >= 1500:
        marginx = 1500

    return render_template('MovingImage.html', marginX=marginx)

@app.route('/boatleft')
def boatleft():
    global marginx
    marginx -= 25
    if marginx <= 0:
        marginx = 0
    return render_template('MovingImage.html', marginX=marginx)

@app.route('/battleship')
def battleship():
    return render_template('Battleship.html')




#Blueprint for battleship grid----------------------
#James's minilab

app.register_blueprint(Blueprints, url_prefix='')

#---------------------------------------------------





#Start Webserver Here
#---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")
#---------------------------------------------------------