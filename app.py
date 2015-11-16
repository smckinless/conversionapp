from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from compute import compute

app = Flask(__name__)

"""def Farenheit2celcius(x):
	return (5 / 9) * (x - 32)
	
def Farenheit2kelvin(x):
	return (5 / 9) * (x + 459.67)
def Celcius2farenheit(x):
	return (9 / 5) * (x + 32)
def Celcius2kelvin(x):
	return x + 273.15
def Kelvin2celcius(x):
	return x - 273.15
def Kelvin2farenheit(x):
	return (x * 9/5) - 459.67"""

class InputForm(Form):
	quantity = FloatField(validators=[validators.InputRequired()])

@app.route('/', methods=['GET','POST'])
def index():
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		quantity = form.quantity.data
		wanted = request.form['wanted']
		conversion = compute(quantity, wanted)
		return render_template('result.html', form=form, conversion=conversion, wanted=wanted)
	else:
		return render_template('conversion.html', form=form)

#@app.route('/result', methods=['POST'])
#def result():
	#quantity = float(request.form['quantity'])
	#conversion = request.form['conversion']
	"""
	if conversion == "FtoC":
		return Farenheit2celcius(quantity)
	
	elif conversion == "FtoK":
		return Farenheit2kelvin(number_given)

	elif conversion == "CtoF":
		return Celcius2farenheit(number_given)

	elif conversion == "CtoK":
		return Celcius2kelvin(number_given)

	elif conversion == "KtoC":
		return Kelvin2celcius(number_given)

	elif conversion =="KtoF":
		return Kelvin2farenheit(number_given)"""
	#return render_template('result.html', quantity=quantity, conversion=conversion)



if __name__ == '__main__':
	app.run()