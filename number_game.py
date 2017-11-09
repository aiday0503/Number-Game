from flask import Flask, render_template
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def setSession():
	session['key'] = random.randrange(1,100)
	session['comment'] = 'Too Low!'

@app.route('/')
def number_game():
	print session['key']
	return render_template('number_game.html')

@app.route('/guess', methods=['POST'])
def guess():
	if str(session['key']) == request.form['guess']:
		return redirect('/winner')
	if str(session['key']) < request.form['guess']:
		session['comment'] = 'Too high!'
		return redirect('/tryagain')
	if str(session['key']) > request.form['guess']:
		session['comment'] = 'Too low!'
		return redirect('/tryagain')

@app.route('/tryagain')
def tryAgain():
	return render_template('again_number.html')
@app.route('/winner')
def winner():
	return render_template('winn_number.html')

@app.route('/reset')
def reset():
	print "Play Again"
	session.pop('key')
	session['key'] = random.randrange(0.100)
	print session['key']
	return redirect('/')
app.run(debug=True)