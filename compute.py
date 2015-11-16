def compute (quantity, wanted):
	if wanted == "FtoC":
		return 5/9 * quantity-32
	
	elif wanted == "FtoK":
		return (5 / 9) * (quantity + 459.67)

	elif wanted == "CtoF":
		return (9 / 5) * (quantity + 32)

	elif wanted == "CtoK":
		return quantity + 273.15

	elif wanted == "KtoC":
		return quantity - 273.15

	elif wanted =="KtoF":
		return quantity * 9/5 - 459.67 