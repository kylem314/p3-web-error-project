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
   # usermessage = db.Column('message', db.String(100))
    username = db.Column(db.String(15), unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    message = db.Column(db.String(100), nullable = False)
    battleshiplocation = db.Column(db.String(5), nullable = False)
    o_battleshiplocation = db.Column(db.String(5), nullable = False)
    startgame = db.Column(db.String(50), nullable = False)
    requested_user = db.Column(db.String(100), nullable = False)


    def __repr__(self):
        return f"User('{self.username}')"


















marginx=0

marginbattleshipx=0
marginbattleshiptop=0



print(marginx)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aboutus')
def aboutus():
        return render_template('aboutus.html')

#404 page
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', body_class = 'page_404' ), 404

@app.route('/movingimage')
def movingimage():
    global marginx
    marginx = 0

    user = session['user']
    
    found_user = maindb.query.filter_by(username=user).first()
    battleshiplocation = found_user.battleshiplocation
    battleshiplocation_o = found_user.o_battleshiplocation
    return render_template('MovingImage.html', battleshiplocation = battleshiplocation, battleshiplocation_o = battleshiplocation_o)



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
        dbcommit = maindb(username = usr, password = pw, message = ' ', battleshiplocation = ' ', startgame = ' ', requested_user = ' ', o_battleshiplocation = ' ')
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
   # session.pop('user', None)
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

            found_user = maindb.query.filter_by(username=user).first()
            Message = found_user.message
            Gameplay = found_user.startgame
            Requesteduser = found_user.requested_user
            battleshiplocation = found_user.battleshiplocation

            if Gameplay == 'True':
                gamet = 'yes'
                return render_template('user.html', email=email, user=user, message = Message, gameplay=Gameplay, gamet = gamet, Requesteduser = Requesteduser, battleshiplocation = battleshiplocation)

            if 'email' in session:
                email = session['email']
        return render_template('user.html', email=email, user=user, message = Message, gameplay=Gameplay, Requesteduser = Requesteduser, battleshiplocation = battleshiplocation)
    else:
        flash('You are not logged in', 'info')
        return redirect(url_for('login'))

@app.route('/message', methods=['POST', 'GET'])
def message():

    if request.method == 'POST':
        
        usr = request.form['msuser']
        msg_user = maindb.query.all()
        user = [user for user in msg_user if user.username == usr][0]

        Message = request.form['msguser']
  #      session['msguser'] = Message
        found_user = maindb.query.filter_by(username=usr).first()
        found_user.message = Message
        db.session.add(found_user)
        db.session.commit()

    return render_template('user.html', usr = usr, ussr=user)




@app.route('/otherpage', methods=["GET", "POST"])
def otherpage():
    if request.method == 'POST':
        signed_user = session['user']
    #    shiplocation = request.form['shiplocation']
        requestuser = request.form['gameuser']

        ship_user = maindb.query.all()
        user = [user for user in ship_user if user.username == requestuser][0]
        found_user = maindb.query.filter_by(username=requestuser).first()
        found_user.startgame = 'True'
        found_user.requested_user = signed_user
        db.session.add(found_user)
        db.session.commit()

        return render_template('otherpage.html', user = user, startgame = 'True', signed_user = signed_user)
    else:
        return render_template('otherpage.html')

    return render_template('otherpage.html', test='Select A Square')

@app.route('/otherpage1', methods=["GET", "POST"])
def otherpage1():
    if request.method == 'POST':
        shiplocation = request.form['shiplocation']
        signed_user = session['user']
        ship_user = maindb.query.all()
        user = [user for user in ship_user if user.username == signed_user][0]
        found_user = maindb.query.filter_by(username=signed_user).first()
        found_user.battleshiplocation = shiplocation
        ruser = found_user.requested_user
        db.session.add(found_user)
        db.session.commit()

        ship_user2 = maindb.query.all()
        user2 = [user for user in ship_user2 if user.username == ruser][0]
        found_user2 = maindb.query.filter_by(username=ruser).first()
        found_user2.o_battleshiplocation = shiplocation
        db.session.add(found_user2)
        db.session.commit()


        return render_template('otherpage.html', shiplocation = shiplocation, user = user, user2 = user2, signed_user = signed_user)
    else:
        return render_template('otherpage.html')

    return render_template('otherpage.html', test='Select A Square')


@app.route('/otherpage2', methods = ['GET', 'POST'])
def otherpage2():

    signed_user = session['user']
    ship_user = maindb.query.all()
    user = [user for user in ship_user if user.username == signed_user][0]
    found_user = maindb.query.filter_by(username=signed_user).first()
    ruser = found_user.requested_user

    ship_user2 = maindb.query.all()
    user2 = [user for user in ship_user2 if user.username == ruser][0]
    found_user2 = maindb.query.filter_by(username=ruser).first()
    found_user2.requested_user = signed_user
    db.session.add(found_user2)
    db.session.commit()
    return render_template('otherpage.html', userT = user, userTT = user2)


@app.route('/otherpage3', methods = ['GET', 'POST'])
def otherpage3():
    signed_user = session['user']
    guess = request.form['gshiplocation']
    ship_user = maindb.query.all()
    user = [user for user in ship_user if user.username == signed_user][0]
    found_user = maindb.query.filter_by(username=signed_user).first()
    location = found_user.o_battleshiplocation
    if guess == location:
        return render_template('otherpage.html', user = user, guess='Hit!')
    else:
        return render_template('otherpage.html', user = user, guess='Miss!')



    return render_template('otherpage.html')


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
    db.session.commit()
    app.run(debug=True, host="127.0.0.1", port="5001")
#---------------------------------------------------------