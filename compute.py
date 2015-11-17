def compute (quantity, wanted):
	if wanted == "FtoC":
		return "{0:.2f}".format(0.55555556 * (quantity - 32))
	
	elif wanted == "FtoK":
		return "{0:.2f}".format(0.55555556 * (quantity + 459.67))

	elif wanted == "CtoF":
		return "{0:.2f}".format((1.8 * quantity) + 32)

	elif wanted == "CtoK":
		return "{0:.2f}".format(quantity + 273.15)

	elif wanted == "KtoC":
		return "{0:.2f}".format(quantity - 273.15)

	elif wanted =="KtoF":
		return "{0:.2f}".format((quantity * 1.8) - 459.67)

	elif wanted == "MtoK":
		return "{0:.2f}".format(quantity * 1.60934)
	
	elif wanted == "KtoM":
		return "{0:.2f}".format(quantity * .621371)

	elif wanted == "ItoF":
		return "{0:.2f}".format(quantity / 12)

	elif wanted == "FtoI":
		return "{0:.2f}".format(quantity * 12)

	elif wanted == "FtoM":
		return "{0:.2f}".format(quantity / 5280)

	elif wanted =="MtoF":
		return "{0:.2f}".format(quantity * 5280)

	elif wanted =="MLtoL":
		return "{0:.2f}".format(quantity / 1000)

	elif wanted =="LtoG":
		return "{0:.2f}".format(quantity * .264172)

	elif wanted =="PtoG":
		return "{0:.2f}".format(quantity * 0.125)

	elif wanted =="PtoQ":
		return "{0:.2f}".format(quantity * 0.5)

	elif wanted =="QtoG":
		return "{0:.2f}".format(quantity * 0.25)