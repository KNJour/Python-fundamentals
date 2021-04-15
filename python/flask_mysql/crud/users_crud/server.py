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

    #DELETE - WORK IN PROGRESS
@app.route('/delete/<int:user_id>')
def delete(user_id):
    query = "DELETE FROM users WHERE ID = %(id)s;"
    data = {
        'id': user_id
    }
    user = connectToMySQL('users_schema').query_db(query,data)
    return redirect ("/")

#SHOW -- 
@app.route('/show/<int:user_id>')
def details_page(user_id):
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        'id': user_id
    }
    user = connectToMySQL('users_schema').query_db(query,data)
    print(user);
    return render_template("details_page.html",user=user[0])

#UPDATE-EDIT - WORK IN PROGRESS
@app.route('/edit/<int:user_id>')
def edit(user_id):
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        'id': user_id
    }
    user = connectToMySQL('users_schema').query_db(query,data)
    print(user);
    return render_template("edit.html",user=user[0])


@app.route('/make_edit/<int:user_id>', methods=['POST'])
def makeEdit(user_id):
    query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": user_id
    }
    user = connectToMySQL('users_schema').query_db(query,data)
    print(user)
    return redirect("/")

##HOME PAGE
@app.route('/')
def readALL():
    query = "SELECT * FROM users;"
    users = connectToMySQL('users_schema').query_db(query)
    print(users)
    return render_template("readAll.html", all_users = users)

if __name__=="__main__":
    app.run(debug=True)