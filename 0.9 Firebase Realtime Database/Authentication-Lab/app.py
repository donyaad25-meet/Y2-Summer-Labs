from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBQ_6qfz2ShK7gkjMkeOY0G60IZLDH2NpU",
    "authDomain": "authen-proj-1db8f.firebaseapp.com",
    "storageBucket": "authen-proj-1db8f.appspot.com",
    "messagingSenderId": "887979677239",
    "appId": "1:887979677239:web:ac4ac3d469775bf12711b2",
    "measurementId": "G-CV6X18Z6CY",
    "databaseURL": "https://authen-proj-1db8f-default-rtdb.europe-west1.firebasedatabase.app/"
}

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY'] = 'super-secret-key'

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/' ,methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        username = request.form['username']
        user2 = {
                "full_name" : full_name,
                "email" : email,
                "username" : username
            }
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            session['quotes'] = []

            UID = session['user']['localId']

            db.child('Users').child(UID).set(user2)
            return redirect(url_for('home'))

        except Exception as e:
            print(e)
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
            return 'error'
    else:
        return render_template('signin.html')

# In the /home route of app.py:

# Delete the code where you stored the quote in the session.
# Create a dictionary called quote that contains the keys 'text' and 'said_by' with values coming from the user inputs.
# Add a key uid to the dictionary quote whose value is the uid of the current user from the session
# Add the quote to the database using the child Quotes with a random key.

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        quote = request.form['quote']
        bywho = request.form['bywho']
        UID = session['user']['localId']

        quoted = {
          "text":quote,
          "said_by":bywho,
          "uid":UID
        }
        db.child("Quotes").push(quoted)
        return redirect(url_for('thanks'))
    else:
        return render_template('home.html')

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():


    return render_template('thanks.html')

@app.route('/display', methods=['GET', 'POST'])
def display():
    quotes = db.child("Quotes").get().val()
    return render_template('display.html', quotes=quotes)

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    session.clear()
    return redirect(url_for('signin'))

if __name__ == "__main__":
    app.run(debug=True)
