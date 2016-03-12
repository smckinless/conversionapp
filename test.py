import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from random import randint

class Convert(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_title(self):
		self.driver.get('http://localhost:5000')
		assert "CONVERSIONS" in self.driver.title

	# To test temperature conversions
	def test_temp_conversion(self):
		numbers = [str(randint(-1000,1000)), str(randint(-1000,1000)), str(randint(-1000,1000))]
		temperature_units = ["Farenheit to Celsius", 
		"Farenheit to Kelvin", 
		"Celsius to Farenheit",
		"Celsius to Kelvin",
		"Kelvin to Celsius",
		"Kelvin to Farenheit"]
		for temperature in temperature_units:
			for number in numbers:
				temperature_conversions = {"Farenheit to Celsius" : ("{0:.2f}".format(0.55555556 * (float(number) - 32))),
					"Farenheit to Kelvin" : ("{0:.2f}".format(0.55555556 * (float(number) + 459.67))), 
					"Celsius to Farenheit" : ("{0:.2f}".format((1.8 * float(number)) + 32)), 
					"Celsius to Kelvin" : ("{0:.2f}".format(float(number) + 273.15)), 
					"Kelvin to Celsius" : ("{0:.2f}".format(float(number) - 273.15)), 
					"Kelvin to Farenheit" : ("{0:.2f}".format((float(number) * 1.8) - 459.67))}
				self.driver.get('http://localhost:5000')
				submission_field = self.driver.find_element_by_id("submission")
				submission_field.send_keys(number)
				select = Select(self.driver.find_element_by_id("categories"))
				select.select_by_visible_text("Temperature")
				temperature_option = Select(self.driver.find_element_by_id("subcats"))
				temperature_option.select_by_visible_text(temperature)
				submit = self.driver.find_element_by_id("submit")
				submit.click()
				time.sleep(2)
				result = self.driver.find_element_by_id("quantity").text
				assert temperature_conversions[temperature] == result

	# To test distance conversions
	def test_dist_conversion(self):
		numbers = [str(randint(-1000,1000)), str(randint(-1000,1000)), str(randint(-1000,1000))]
		distance_units = ["Miles to Kilometers", 
		"Kilometers to Miles", 
		"Inches to Feet",
		"Feet to Inches",
		"Feet to Miles",
		"Miles to Feet"]
		for distance in distance_units:
			for number in numbers:
				distance_conversions = {"Miles to Kilometers" : ("{0:.2f}".format(float(number) * 1.60934)),
					"Kilometers to Miles" : ("{0:.2f}".format(float(number) * .621371)), 
					"Inches to Feet" : ("{0:.2f}".format(float(number) / 12)), 
					"Feet to Inches" : ("{0:.2f}".format(float(number) * 12)), 
					"Feet to Miles" : ("{0:.2f}".format(float(number) / 5280)), 
					"Miles to Feet" : ("{0:.2f}".format(float(number) * 5280))}
				self.driver.get('http://localhost:5000')
				submission_field = self.driver.find_element_by_id("submission")
				submission_field.send_keys(number)
				select = Select(self.driver.find_element_by_id("categories"))
				select.select_by_visible_text("Distance")
				distance_option = Select(self.driver.find_element_by_id("subcats"))
				distance_option.select_by_visible_text(distance)
				submit = self.driver.find_element_by_id("submit")
				submit.click()
				time.sleep(2)
				result = self.driver.find_element_by_id("quantity").text
				assert distance_conversions[distance] == result

	# To test volume conversions
	def test_volume_conversion(self):
		numbers = [str(randint(-1000,1000)), str(randint(-1000,1000)), str(randint(-1000,1000))]
		volume_units = ["Milliliters to Liters", 
		"Liters to Gallons", 
		"Pints to Gallons",
		"Pints to Quarts",
		"Quarts to Gallons"]
		for volume in volume_units:
			for number in numbers:
				volume_conversions = {"Milliliters to Liters" : ("{0:.2f}".format(float(number) / 1000)),
					"Liters to Gallons" : ("{0:.2f}".format(float(number) * .264172)), 
					"Pints to Gallons" : ("{0:.2f}".format(float(number) * 0.125)), 
					"Pints to Quarts" : ("{0:.2f}".format(float(number) * 0.5)), 
					"Quarts to Gallons" : ("{0:.2f}".format(float(number) * 0.25))}
				self.driver.get('http://localhost:5000')
				submission_field = self.driver.find_element_by_id("submission")
				submission_field.send_keys(number)
				select = Select(self.driver.find_element_by_id("categories"))
				select.select_by_visible_text("Volume")
				volume_option = Select(self.driver.find_element_by_id("subcats"))
				volume_option.select_by_visible_text(volume)
				submit = self.driver.find_element_by_id("submit")
				submit.click()
				time.sleep(2)
				result = self.driver.find_element_by_id("quantity").text
				assert volume_conversions[volume] == result
		

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()