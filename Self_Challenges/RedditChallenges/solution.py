'''
	solution.py
	Decided to do this in Python, since it appeals
	to perform list/array manipulation in Python 
	rather than Java.
'''

import unittest

class Test(unittest.TestCase):
	
	data = [()]
	
	
	def test_solution(self):
		for [case, expected] in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
