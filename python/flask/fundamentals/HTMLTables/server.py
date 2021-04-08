from flask import Flask,app, render_template,request
app = Flask(__name__)    
@app.route('/')    

def userTable():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Bobby', 'last_name' : 'Brown'},
        {'first_name' : 'Jimmy', 'last_name' : 'Cricket'},
        {'first_name' : 'Mr.', 'last_name' : 'Man'}
    ]
    return render_template("user.html", users=users)

    
if __name__=="__main__":       
    app.run(debug=True)   