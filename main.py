from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/otherpage')
def otherpage():
    return render_template('otherpage.html')

@app.route('/a1')
def a1():
    return render_template('otherpage.html', test='a1')

@app.route('/a2')
def a2():
    return render_template('otherpage.html', test='a2')

@app.route('/a3')
def a3():
    return render_template('otherpage.html', test='a3')

@app.route('/a4')
def a4():
    return render_template('otherpage.html', test='a4')



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")