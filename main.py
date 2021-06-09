import flask
from flask import Flask, render_template, request, redirect, url_for, session, flash
from minilabs.aidanminilab import aminilab_bp
from minilabs.tylerminilab import tylerminilab_bp
from minilabs.jamesminilab import jamesminilab_bp
from minilabs.kyleminilab import kyleminilab_bp
from minilabs.calvinminilab import calvinminilab_bp
from blueprints import Blueprints
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


#Minilab blueprint registry
#-----------------------------------------------------
app = Flask(__name__)
app.register_blueprint(aminilab_bp, url_prefix='/aidanminilab')
app.register_blueprint(calvinminilab_bp, url_prefix='/calvinminilab')
app.register_blueprint(tylerminilab_bp, url_prefix='/tylerminilab')
app.register_blueprint(jamesminilab_bp, url_prefix='/jamesminilab')
app.register_blueprint(kyleminilab_bp, url_prefix='/kyleminilab')
#-----------------------------------------------------



#Session/Database Stuff
#-----------------------------------------------------
app.secret_key = 'THUOenqf52fDj2'
app.permanent_session_lifetime = timedelta(minutes=30)
#-----------------------------------------------------






#Database Setup
#-----------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class maindb(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))
    username = db.Column(db.String(15), unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"User('{self.username}')"


















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

@app.route('/easter')
def easter():
    return render_template('easter.html')

@app.route('/jamesm')
def Jminilab():
    return render_template('James Bubble Sort.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/MessageBoard')
def MessageBoard():
    return render_template('MessageBoard.html')



#Blueprint for battleship grid----------------------
#James's minilab

app.register_blueprint(Blueprints, url_prefix='')

#---------------------------------------------------

#imports











#Session/Database


@app.route('/Blogin', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #query database and set up session
        users = maindb.query.all()
        session.pop('user_id', None)
        session.permanent = True

        #retrieve username and password from html
        username = request.form['username']
        password = request.form['password']

        #check if username and password match
        try:
            user = [user for user in users if user.username == username][0]
            #successful login
            if user and user.password == password:
                session['user'] = user.username
                flash("You have been logged in")
                return redirect(url_for('user'))
            #incorrect username/password
            else:
                flash("User is incorrect or does not exist.")
                return redirect(url_for('login'))
        except:
            flash("Password or Username is incorrect or does not exist.")
            return redirect(url_for('login'))
    else:
        if 'user' in session:
            flash("You are already logged in")
            return redirect(url_for('user'))
        return render_template('login.html', insession = False)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == "POST":
        #retrieve username and password from html
        usr = request.form.get('username')
        pw = request.form.get('password')
        #commit username and password to database
        dbcommit = maindb(username = usr, password = pw)
        db.session.add(dbcommit)
        db.session.commit()
        flash("New account successfully created")
        #send user back to login
        return redirect(url_for('login'))
    #render template
    flash("Create a new account")
    return render_template('register.html', insession = False)

@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            found_user = maindb.query.filter_by(name=user).first()  #changes users email
            found_user.email = email
            db.session.commit()
            flash('Email was saved')
        elif request.method == 'GET':
            if 'email' in session:
                email = session['email']
        return render_template('user.html', email=email, user=user)
    else:
        flash('You are not logged in', 'info')
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f'{user}, Logout Successfull', 'info')
    else:
        flash('You are not logged in', 'info')
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

#webapi
import requests

@app.route('/news')
def news():
    #twitter embed api url
    urldnhs = "https://publish.twitter.com/oembed?url=https://twitter.com/dnhsnighthawks"
    urlpoway = "https://publish.twitter.com/oembed?url=https://twitter.com/powayunified"
    responsednhs = requests.get(urldnhs)
    responsepoway = requests.get(urlpoway)
    #set url value in json to variable
    jsonurldnhs = responsednhs.json()['url']
    jsonurlpoway = responsepoway.json()['url']
    return flask.render_template("news.html", jsonurldnhs=jsonurldnhs, jsonurlpoway=jsonurlpoway)















#Start Webserver Here
#---------------------------------------------------------
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="127.0.0.1", port="5001")
#---------------------------------------------------------