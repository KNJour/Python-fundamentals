from flask import Flask, render_template, request,session,redirect
from mysqlconnection  import connectToMySQL
app = Flask(__name__)
app.secret_key = "Benny Bob wuz heer."
#sends to new user page
@app.route('/newUser')
def newUser():

    return render_template("create.html");

#takes info from newUser page and adds it
@app.route('/create', methods=['POST'])
def createUser():
    mysql = connectToMySQL("users_schema")
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(firstname)s, %(lastname)s, %(email)s, NOW(), NOW());"
    print(query)
    data = {
        "firstname": request.form["first_name"],
        "lastname": request.form["last_name"],
        "email": request.form["email"]
    }
    new_user_id = mysql.query_db(query, data)
    return redirect("/")

@app.route('/')
def readALL():
    mysql = connectToMySQL('users_schema')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("readAll.html", all_users = users)




if __name__=="__main__":
    app.run(debug=True)