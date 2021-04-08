from flask import Flask,app,render_template, request
app = Flask(__name__)

#index route or endpoint
@app.route("/")
def index():
    # return "Hello World!"
    return render_template("index.html")

@app.route("/users")
def users():
    db_users = [ 
        {"first_name":"Keith", "last_name":"Journell", "email":"k@dojo.com"},
        {"first_name":"Bob", "last_name":"McBob", "email":"k@dorp.com"},
        {"first_name":"Benny", "last_name":"Bens", "email":"bbens@bens.com"},
        {"first_name":"Jaque", "last_name":"Brown", "email":"jbrown@j.com"},
        {"first_name":"sally", "last_name":"sal", "email":"SSAL@dojo.com"}
    ]
    return render_template("users.html", users=db_users)

@app.route("/add_user")
def add_user():
    return render_template("add_user.html")
#post defines that we accept the method fo POST

@app.route("/create/user",methods=['POST'])
def create_user():
    print(request.form)
    print(request.form['first_name'])
    print(request.form['last_name'])
    print(request.form['email'])

if __name__=="__main__":
    # Method that starts our flask server
    #we give it an argument to debug
    app.run(debug=True)