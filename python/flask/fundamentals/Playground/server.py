from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/play')
def playhome():
    return render_template("index.html")


@app.route('/play/<int:num>')
def play(num):
    return render_template("play.html", x=num)

@app.route('/play/<int:num>/<string:color>')
def playColor(num,color):
    return render_template("playcolor.html", x=num, color=color)
if __name__=="__main__":
    app.run(debug=True)