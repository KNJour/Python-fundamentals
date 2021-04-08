from flask import Flask,app, render_template, request
app = Flask(__name__)    
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/<int:x>/')
def next(x):
    return render_template("next.html", num1=int(x))

@app.route('/<int:x>/<int:y>')
def last(x,y):
    return render_template("last.html", num1=x, num2=y)

if __name__=="__main__":  
    app.run(debug=True)