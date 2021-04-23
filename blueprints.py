from flask import Blueprint, render_template

from minilabs.jamesminilab.classb import Battleship, HP, BoatHealth, Boatstats

Blueprints = Blueprint('blueprints', __name__, static_folder='static', template_folder='templates')

Var2 = Battleship('12', HP, 'Destroyer')

Boathealth = Var2.hp()




@Blueprints.route('/hp')
def hp():
    info = []
    info.append(Battleship('12', HP, 'Destroyer'))
    global Var2
    return render_template('otherpage.html', HP = BoatHealth)

@Blueprints.route('/stats')
def stats():
    return render_template('otherpage.html', stats = Boatstats)


#A routes start here
#----------------------------------------------------------------------------------------------------------

@Blueprints.route('/a1')
def a1():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 6.35
    marginbattleshipx = 36.5

    return render_template('otherpage.html', test='a1', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@Blueprints.route('/a2')
def a2():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 6.35
    marginbattleshipx = 46.5
    return render_template('otherpage.html', test='a2', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@Blueprints.route('/a3')
def a3():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 6.35
    marginbattleshipx = 56.5
    return render_template('otherpage.html', test='a3', marginX = marginbattleshipx, marginT = marginbattleshiptop)


@Blueprints.route('/a4')
def a4():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 6.35
    marginbattleshipx = 66.5
    return render_template('otherpage.html', test='a4', marginX = marginbattleshipx, marginT = marginbattleshiptop)

#B routes start here
#----------------------------------------------------------------------------------------------------------

@Blueprints.route('/b1')
def b1():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 12.7
    marginbattleshipx = 36.5

    return render_template('otherpage.html', test='b1', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@Blueprints.route('/b2')
def b2():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 12.7
    marginbattleshipx = 46.5
    return render_template('otherpage.html', test='b2', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@Blueprints.route('/b3')
def b3():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 12.7
    marginbattleshipx = 56.5
    return render_template('otherpage.html', test='b3', marginX = marginbattleshipx, marginT = marginbattleshiptop)


@Blueprints.route('/b4')
def b4():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 12.7
    marginbattleshipx = 66.5
    return render_template('otherpage.html', test='b4', marginX = marginbattleshipx, marginT = marginbattleshiptop)


#C routes start here
#----------------------------------------------------------------------------------------------------------

@Blueprints.route('/c1')
def c1():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 19.05
    marginbattleshipx = 36.5

    return render_template('otherpage.html', test='c1', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@Blueprints.route('/c2')
def c2():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 19.05
    marginbattleshipx = 46.5
    return render_template('otherpage.html', test='c2', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@Blueprints.route('/c3')
def c3():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 19.05
    marginbattleshipx = 56.5
    return render_template('otherpage.html', test='c3', marginX = marginbattleshipx, marginT = marginbattleshiptop)


@Blueprints.route('/c4')
def c4():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 19.05
    marginbattleshipx = 66.5
    return render_template('otherpage.html', test='c4', marginX = marginbattleshipx, marginT = marginbattleshiptop)

#D routes start here
#-------------------------------------------------------------------------------------------------------------------------

@Blueprints.route('/d1')
def d1():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 25.4
    marginbattleshipx = 36.5

    return render_template('otherpage.html', test='d1', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@Blueprints.route('/d2')
def d2():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 25.4
    marginbattleshipx = 46.5
    return render_template('otherpage.html', test='d2', marginX = marginbattleshipx, marginT = marginbattleshiptop)

@Blueprints.route('/d3')
def d3():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 25.4
    marginbattleshipx = 56.5
    return render_template('otherpage.html', test='d3', marginX = marginbattleshipx, marginT = marginbattleshiptop)


@Blueprints.route('/d4')
def d4():
    global marginbattleshiptop
    global marginbattleshipx

    marginbattleshiptop = 25.4
    marginbattleshipx = 66.5
    return render_template('otherpage.html', test='d4', marginX = marginbattleshipx, marginT = marginbattleshiptop)
