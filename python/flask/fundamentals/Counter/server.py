from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def home():
    print("reached home!")
    print(request.form)
    return render_template("index.html", counter=count)

# @app.route('/increment', methods=['POST'])
# def increment():
#     i = i + 1
#     return redirect

@app.route('/process', methods=['POST'])
def process():
    session['count'] = request.form['count']
    print(f"count updated to {i}")
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

# @app.route("/show")
# def show_user():
#     print("showing the user info from the form")
#     print(request.form)
#     return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)