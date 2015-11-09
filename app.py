from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def calcs():
	def Farenheit2celcius(x):
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
		return (x * 9/5) - 459.67

	number_given = 0
	unit_given = 0
	unit_wanted = 0

	if unit_given == "Farenheit":
		if unit_wanted == "Celcius":
			return Farenheit2celcius(number_given)

		elif unit_wanted == "Kelvin":
			return Farenheit2kelvin(number_given)

	elif unit_given == "Celcius":
		if unit_wanted == "Farenheit":
			return Celcius2farenheit(number_given)

		elif unit_wanted == "Kelvin":
			return Celcius2kelvin(number_given)

	else
		if unit_wanted == "Celcius":
			return Kelvin2celcius(number_given)

		else
			return Kelvin2farenheit(number_given)
	return render_template('index.html')


if __name__ == '__main__':
	app.run()