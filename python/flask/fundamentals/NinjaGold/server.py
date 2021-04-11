from flask import Flask, render_template, session, request, redirect
import random, datetime
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def ninja_gold():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session: 
        session['activities']  = []
        session['oppositeday'] = []

    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def processMoney():
    if (request.form['option'] == 'farm'):
        session['tendies'] = random.randint(10,20)
        session['activities'].append([f"Earned {session['tendies']} gold from the Farm! ({datetime.datetime.now().strftime('%c')})","green"])
    elif (request.form['option'] == 'cave'):
        session['tendies'] = random.randint(5,10)
        session['activities'].append([f"Earned {session['tendies']} gold from the Cave! ({datetime.datetime.now().strftime('%c')})","green"])

    elif (request.form['option'] == 'house'):
        session['tendies'] = random.randint(1,5)
        session['activities'].append([f"Earned {session['tendies']} gold from the House! ({datetime.datetime.now().strftime('%c')})","green"])

    elif (request.form['option'] == 'casino'):
        session['tendies'] = random.randint(-50,50)
        if (session['tendies'] > 0):
            session['activities'].append([f"Earned {session['tendies']} gold from the Casino! ({datetime.datetime.now().strftime('%c')})","green"])
        else:
            session['activities'].append([f"Lost {session['tendies']*-1} gold from the Casino! You suck! ({datetime.datetime.now().strftime('%c')})","red"])
    elif (request.form['option'] == 'reset'):
        session['tendies'] = 0
        session['gold'] = 0
        session['activities']  = []
    
    print(session['tendies'])
    print(session['activities'])
    session['gold'] += session['tendies']
    session['oppositeday'] = session['activities']
    session['oppositeday'].reverse()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)