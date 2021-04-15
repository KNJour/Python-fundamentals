from flask import Flask, render_template, redirect, request
app = Flask(__name__)
from mysqlconnection  import connectToMySQL
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create():
    query = "INSERT INTO burgers (name,bun,meat,calories,topping_one,topping_two,created_at,updated_at) VALUES (%(name)s,%(bun)s,%(meat)s,%(calories)s,%(topping_one)s,%(topping_two)s, NOW(), NOW())"
    data = {
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        "topping_one": request.form['topping_one'],
        "topping_two": request.form['topping_two']
    }
    mysql = connectToMySQL('burgers')
    mysql.query_db(query,data)
    return redirect('/burgers')

@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    query = "SELECT * FROM burgers WHERE id = %(id)s;"
    data = {
        'id': burger_id
    }
    burger = connectToMySQL('burgers').query_db(query,data)
    print(burger)
    return render_template("details_page.html", burger=burger)

@app.route('/burgers')
def burgers():
    query = "SELECT * FROM burgers;"
    burger = connectToMySQL('burgers').query_db(query)
    print(burgers)
    return render_template("results.html", all_burgers=burgers)

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    query = "UPDATE burgers SET name=%(name)s,bun=%(bun)s,meat=%(meat)s,calories=%(calories)s,topping_one=%(topping_one)s,topping_two=%(topping_two)s, updated_at = NOW() WHERE id = %(id)s;"
    data = {
        'id': burger_id,
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        "topping_one": request.form['topping_one'],
        "topping_two": request.form['topping_two']
    }

    burger = connectToMySQL('burgers').query_db(query,data)
    print(burger)
    return redirect(f"/show/{burger_id}")
# delete
app.route('/delete/<int:burger_id>')
def delete():
    query = "DELETE FROM burgers WHERE id = %(id)s;"
    data = {
        'id': burger_id
    }
    print(burger)
    burger = connectToMySQL('burgers').query_db(query,data)
    return redirect("/burgers")

@app.route('/create/topping', methods=['POST'])
def create_topping():
    query = "INSERT INTO toppings (name, created_at, updated_at, burger_id) VALUES (%(name)s, NOW(),NOW(),%(burger_id)s);"
    data = {
        "burger_id": request.form['burger_id'],
        "name": request.form['name']
    }

    connectToMySQL('burgers').query_db(query,data)
    return redirect(f"/show/{request.form['burger_id']}")
@app.route('/show/<int:burger_id>')
def edit_page(burger_id):
    query = "SELECT * FROM toppings JOIN burgers ON burgers.id = toppings.burger_id WHERE burgers.id = %(id)s;"
    data = {
        'id': burger_id
    }
    burger = connectToMySQL('burgers').query_db(query,data)
    return render_template()
if __name__=="__main__":
    app.run(debug=True)
