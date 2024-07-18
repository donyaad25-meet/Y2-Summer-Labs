from flask import Flask, render_template, request, url_for, redirect
import random
app = Flask(__name__)
   
@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method=='POST':
		birthmonth=request.form['birthmonth']
		return redirect(url_for('fortune', birthmonth=birthmonth))

	return render_template("home.html")

@app.route('/fortune')
def fortune():
	fortunes_options=["You will succeed in your life", "You will finish your CS lab easily",
	"Everyday in your life is a special occasion", "You will win the Oscar"
	, "Cats will come to you when you pespes","You will always be surrounded by true friends", "Plan for many pleasures ahead"
	,"Happy News is on its way", "You are kind and friendly","You will receive money from an unexpected source"]
	random_fortune=random.choice(fortunes_options)
	return render_template('fortune.html', fortune=random_fortune)

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