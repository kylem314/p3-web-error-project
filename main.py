from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/otherpage')
def otherpage():
    return render_template('otherpage.html')





if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")