from flask import Flask, render_template, request, redirect, url_for, session, flash
from minilabs.aidanminilab import aidanminilab_bp
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
app.register_blueprint(aidanminilab_bp, url_prefix='/aidanminilab')
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



class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


















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

#Blueprint for battleship grid----------------------
#James's minilab

app.register_blueprint(Blueprints, url_prefix='')

#---------------------------------------------------










#Session/Database


@app.route('/Blogin', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email

        else:
            usr = users(user, '')
            db.session.add(usr)
            db.session.commit()
        flash(f'Login Successfull, {user}', 'info')
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            user = session['user']
            flash(f'{user}, you are already logged in', 'info')
            return redirect(url_for('user'))
        return render_template('Battleship.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            found_user = users.query.filter_by(name=user).first()  #changes users email
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

















#Start Webserver Here
#---------------------------------------------------------
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="127.0.0.1", port="5001")
#---------------------------------------------------------