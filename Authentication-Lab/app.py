from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBQ_6qfz2ShK7gkjMkeOY0G60IZLDH2NpU",
    "authDomain": "authen-proj-1db8f.firebaseapp.com",
    "storageBucket": "authen-proj-1db8f.appspot.com",
    "messagingSenderId": "887979677239",
    "appId": "1:887979677239:web:ac4ac3d469775bf12711b2",
    "measurementId": "G-CV6X18Z6CY",
    "databaseURL": ""
}

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY'] = 'super-secret-key'

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/' ,methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            session['quotes'] = []
            return redirect(url_for('home'))

        except Exception as e:
            return "error"
    else:
        return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            session['quotes'] = []
            return redirect(url_for('home'))

        except:
            return 'Welcome'
    else:
        return render_template('signin.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
    	quote = request.form['quote']

    	session['quotes'].append(quote)  
    	session.modified = True

    	return redirect(url_for('thanks'))
    return render_template('home.html')

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html')

@app.route('/display', methods=['GET', 'POST'])
def display():
    if 'user' not in session:
        return redirect(url_for('signin'))
    quotes = session.get('quotes', [])
    return render_template('display.html', quotes=quotes)

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    session.clear()
    return redirect(url_for('signin'))

if __name__ == "__main__":
    app.run(debug=True)
