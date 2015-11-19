from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from compute import compute

app = Flask(__name__)


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




if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)