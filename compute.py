def compute (quantity, wanted):
	if wanted == "FtoC":
		return 0.55555556 * (quantity - 32)
	
	elif wanted == "FtoK":
		return 0.55555556 * (quantity + 459.67)

	elif wanted == "CtoF":
		return 1.8 * (quantity - 32)

	elif wanted == "CtoK":
		return quantity + 273.15

	elif wanted == "KtoC":
		return quantity - 273.15

	elif wanted =="KtoF":
		return (quantity * 1.8) - 459.67 