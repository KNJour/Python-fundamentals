`from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# @app.route('/users', methods=['POST'])

# def create_user():
#     print("Got Post Info")
#     #Here we add two properties to session to store the name and email
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')


# ALWAYS REDIRECT ON A POST ROUTE
@app.route('/process',methods=['POST'])
def process():
    sesson['name'] = request.form['name']
    session['bun'] = request.form['bun']
    session['meat'] = request.form['meat']
    session['calories'] = request.form['calories']
    session['topping_one'] = request.form['topping_one']
    session['topping_two'] = request.form['topping_two']
    return redirect('/burger')

@app.route('/burger')
def burger():
    lunch = {
        "name" : session['name'],
        "bun" : session['bun'],
        "meat" : session['meat'],
        "calories" : session['calories'],
        "topping_one" : session['topping_one'],
        "topping_two" : session['topping_two']
    }
    return render_template("burger.html", )

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)