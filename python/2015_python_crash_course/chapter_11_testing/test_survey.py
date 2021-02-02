# assertEqual(a, b)
# assertNotEqual(a, b)
# assertTrue(a)
# assertFalse(a)
# assertIn(item, list)
# assertNotIn(item, list)

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	
	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test cases.
		"""
		
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['C', 'Java', 'C++']
	
	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
		
	def test_store_three_responses(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()