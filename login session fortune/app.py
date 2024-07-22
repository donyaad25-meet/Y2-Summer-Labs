from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session
import random

app = Flask(__name__)
app.config['SECRET_KEY']="PASSWORD"

			
@zpp.route('/', methods=['GET', 'POST'])
def login():
	if request.method=='POST':
		session['name']= request.form['name']
		session['birthname']= request.form['birthname']
		return redirect(url_for('home'))
	return render_template('login.html')			


@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method=='POST':
		birthmonth=request.form['birthmonth']
		return redirect(url_for('fortune', birthmonth=birthmonth))

	return render_template("home.html")

	if 'name' in session and 'birthmonth' in session:
		return render_template('home.html', name=session['name'])
	else:
		return redirect(url_for('login'))


@app.route('/fortune')
def fortune():
	fortunes_options=["You will succeed in your life", "You will finish your CS lab easily",
	"Everyday in your life is a special occasion", "You will win the Oscar"
	, "Cats will come to you when you pespes","You will always be surrounded by true friends", "Plan for many pleasures ahead"
	,"Happy News is on its way", "You are kind and friendly","You will receive money from an unexpected source"]
	random_fortune=random.choice(fortunes_options)
	return render_template('fortune.html', fortune=random_fortune)

	if 'name' in session and 'birth_month' in session:
		fortune= "Your fortune is {} born in {}.".format(session['name'], session['birth_month'])
		return render_template('fortune.html', fortune=fortune)
  	else:
        return redirect(url_for('login'))


	index= len(birthmonth) % len(fortunes_options)
	thefortunes=fortunes_options[index]

	return render_template('fortune.html', fortune=thefortunes)

@app.route('/userinput', methods=['POST', 'GET'])
def userinput():
	if request.method ==' GET ':
		return render_template('form.html')
	else :
		name = request.form['birthmonth']	
		return redirect(url_for('fortune'))

if __name__ == '__main__':
    app.run(debug = True)   