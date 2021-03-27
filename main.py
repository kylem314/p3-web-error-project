from flask import Flask, render_template, url_for, request, redirect, session, flash

##import api
import bulkofproject.billboardAPI as billboardAPI
#import models
import database

app = Flask(__name__)


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


#A routes start here
#----------------------------------------------------------------------------------------------------------

@app.route('/a1')
def a1():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 6.35
    marginbattleshipx = 36.5

    return render_template('otherpage.html', test='a1', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@app.route('/a2')
def a2():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 6.35
    marginbattleshipx = 46.5
    return render_template('otherpage.html', test='a2', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@app.route('/a3')
def a3():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 6.35
    marginbattleshipx = 56.5
    return render_template('otherpage.html', test='a3', marginX = marginbattleshipx, marginT = marginbattleshiptop)


@app.route('/a4')
def a4():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 6.35
    marginbattleshipx = 66.5
    return render_template('otherpage.html', test='a4', marginX = marginbattleshipx, marginT = marginbattleshiptop)

#B routes start here
#----------------------------------------------------------------------------------------------------------

@app.route('/b1')
def b1():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 12.7
    marginbattleshipx = 36.5

    return render_template('otherpage.html', test='b1', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@app.route('/b2')
def b2():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 12.7
    marginbattleshipx = 46.5
    return render_template('otherpage.html', test='b2', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@app.route('/b3')
def b3():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 12.7
    marginbattleshipx = 56.5
    return render_template('otherpage.html', test='b3', marginX = marginbattleshipx, marginT = marginbattleshiptop)


@app.route('/b4')
def b4():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 12.7
    marginbattleshipx = 66.5
    return render_template('otherpage.html', test='b4', marginX = marginbattleshipx, marginT = marginbattleshiptop)


#C routes start here
#----------------------------------------------------------------------------------------------------------

@app.route('/c1')
def c1():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 19.05
    marginbattleshipx = 36.5

    return render_template('otherpage.html', test='c1', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@app.route('/c2')
def c2():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 19.05
    marginbattleshipx = 46.5
    return render_template('otherpage.html', test='c2', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@app.route('/c3')
def c3():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 19.05
    marginbattleshipx = 56.5
    return render_template('otherpage.html', test='c3', marginX = marginbattleshipx, marginT = marginbattleshiptop)


@app.route('/c4')
def c4():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 19.05
    marginbattleshipx = 66.5
    return render_template('otherpage.html', test='c4', marginX = marginbattleshipx, marginT = marginbattleshiptop)

#D routes start here
#-------------------------------------------------------------------------------------------------------------------------

@app.route('/d1')
def d1():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 25.4
    marginbattleshipx = 36.5

    return render_template('otherpage.html', test='d1', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@app.route('/d2')
def d2():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 25.4
    marginbattleshipx = 46.5
    return render_template('otherpage.html', test='d2', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@app.route('/d3')
def d3():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 25.4
    marginbattleshipx = 56.5
    return render_template('otherpage.html', test='d3', marginX = marginbattleshipx, marginT = marginbattleshiptop)


@app.route('/d4')
def d4():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 25.4
    marginbattleshipx = 66.5
    return render_template('otherpage.html', test='d4', marginX = marginbattleshipx, marginT = marginbattleshiptop)


#Login or Making New Accounts
#---------------------------------------------------------
@app.route('/login', methods = ['POST', 'GET'])
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
        dbcommit = maindb(username = usr, password = pw, song = "none", artist = "none")
        db.session.add(dbcommit)
        db.session.commit()
        flash("New account successfully created")
        #send user back to login
        return redirect(url_for('login'))
    #render template
    flash("Create a new account")
    return render_template('register.html', insession = False)

#Start Webserver Here
#---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")
#---------------------------------------------------------