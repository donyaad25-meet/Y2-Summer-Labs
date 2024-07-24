from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDXEvVjAfwcdPyLsX2ei73H3z71T4Q9Z0I",
  "authDomain": "website-88135.firebaseapp.com",
  "projectId": "website-88135",
  "storageBucket": "website-88135.appspot.com",
  "messagingSenderId": "772301892497",
  "appId": "1:772301892497:web:8cfa0bc48ab859c03a0830",
  "measurementId:":"G-QHSBPXRYMF",
  "databaseURL": "https://website-88135-default-rtdb.europe-west1.firebasedatabase.app/"
}

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY'] = 'super-secret-key'		

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if request.method=='POST':
		name= request.form['name']
		email= request.form['email']
		password= request.form['password']
		user_db= {
		"name": name,
		"email": email
		}
		try:
			user_auth = auth.create_user_with_email_and_password(email, password)
			session['user']= user_auth
			UID= session['user']['localId']
			db.child('users').child(UID).set(user_db)
			return redirect(url_for('home.html'))
		except:
			return render_template('welcome.html')
	else:
		return render_template('signup.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method== 'POST':
		email= request.form['email']
		password= request.form['password']
		return render_template('welcome.html')
	else:
		return render_template('login.html')	
@app.route('/sucs', methods=['POST','GET'])
def sucs():
	if request.method== 'GET':
		return render_template('sucsubmit.html')

@app.route('/show', methods=['POST', 'GET'])
def show():
	if request.method== 'POST':
		showname = request.form.get('showname')
		email= request.form.get('email')
		homepage= request.form.get('homepage')
		password= request.form.get('password')
		links= {
		"showname": showname,
		"homepage": homepage,
		# "text": summary
		}
		try:
			db.child('links').child(UID).push(links)
			# session['links']= links
			UID= session['user']['localId']
			# user= db.child("Users").child(UID).get().val()
			return redirect(url_for('sucs'))
		except:
			return render_template('sucsubmit.html')
	else:
		return render_template('addshow.html')	

@app.route('/display', methods=['GET', 'POST'])
def display():
    posts = db.child("links").get().val()
    return render_template('display.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
