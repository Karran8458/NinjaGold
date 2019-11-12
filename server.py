from flask import Flask, render_template, request, redirect, session # added request
import random
app = Flask(__name__)
app.secret_key = 'randomstring'
c=0
status = " "
@app.route('/')
def index():
    global c
    global status
    return render_template("index.html", counter = c, status_form = status)
    
@app.route('/process_money', methods=['POST'])
def far():
    global c
    global status
    status = " "
    if request.form['which_form'] == 'farm':
      farm = random.randint(10, 20)
      status = "Earned " + str(farm) + " golds from Farm"
      c += farm
    elif request.form['which_form'] == 'cave':
      cave = random.randint(5, 10)
      status = "Earned " + str(cave) + " golds from Cave"
      c += cave
    elif request.form['which_form'] == 'house':
      house = random.randint(2, 5)
      status = "Earned " + str(house) + " golds from House"
      c += house
    elif request.form['which_form'] == 'casino':
      if random.random() < 0.5:
        casino = random.randint(0, 50)
        status = "Entered a casino and won " + str(casino) + " golds"
        c += casino
      else:
        casino = random.randint(0, 50)
        status = "Entered a casino and lost " + str(casino) + " golds... Ouch..."
        c -= casino
    return redirect("/")
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

