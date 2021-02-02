import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""
	
	def test_first_last_name(self):
		"""Do names like 'Angshu Zaman' work?"""
		formatted_name = get_formatted_name('angshu', 'zaman')
		self.assertEqual(formatted_name, 'Angshu Zaman')
		
	def test_first_middle_last(self):
		"""Do names like 'Angshu Ahnaf Zaman' work?"""
		formatted_name = get_formatted_name('angshu', 'zaman', 'ahnaf')
		self.assertEqual(formatted_name, 'Angshu Ahnaf Zaman')

unittest.main()
