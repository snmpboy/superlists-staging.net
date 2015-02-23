from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retreive_it_later(self):
    	#Edith has heard about a cool new online to-do app. She goes to check its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do listss
		self.assertIn('To-Do' in self.browser.title)
		self.fail('Finish the test')

if __name__ == '__main__':
	unittest.main(warnings='ignore')