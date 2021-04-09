from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect ('/results')
@app.route('/results')
def results():
    dojo = { 
        "name" : session['name'],
        "location" : session['location'],
        "language" : session['language'],
        "name" : session['name'],
    }
    return render_template("results.html")
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")

if __name__ == "__main__":
    app.run(debug=True)