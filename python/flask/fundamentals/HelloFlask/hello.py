from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", phrase="hello", times=5)
    
@app.route('/success')
def success():
    return "success"

@app.route("/<name>")
def hello_person(name):
    return "Hello " + name

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello," + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and idcopy
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
    
    # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.