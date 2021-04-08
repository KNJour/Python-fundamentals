from flask import Flask,app,render_template, request
app = Flask(__name__)
@app.route("/")
def helloWorld():
    print("Hello World")
    return "Hello World"

@app.route("/dojo/")
def dojo():
    return "dojo"

@app.route("/say/<name>")
def sayName(name):
    print("Hi " + name)
    return "Hi " + name

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

@app.route("/repeat/<int:num>/<thing>")
def repeatIt(num, thing):
    x = int(num)
    return render_template("repeat.html", num=x, thing=thing)
@app.route("/<name>")
def justname(name):
    print()("Hi " + name)
    return "Hi " + name

if __name__=="__main__":
    app.run(debug=True)
