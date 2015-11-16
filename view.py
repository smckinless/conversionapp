import sys
import compute

def get_input():
	quantity = float(sys.argv[1])
	return quantity

def output():
	conversion = compute.compute(quantity)
	print conversion