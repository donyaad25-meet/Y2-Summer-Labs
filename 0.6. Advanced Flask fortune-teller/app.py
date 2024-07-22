from flask import Flask, render_template
import random
app = Flask(__name__)
   
@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/fortune')
def fortune():
	fortunes_options=["You will succeed in your life", "You will finish your CS lab easily",
	"Everyday in your life is a special occasion", "You will win the Oscar", "Cats will come to you when you pespes",]
	random_fortune=random.choice(fortunes_options)
	return render_template('fortune.html', fortune=random_fortune)




if __name__ == '__main__':
    app.run(debug = True)   