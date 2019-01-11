'''
	solution.py
	Decided to do this in Python, since it appeals
	to perform list/array manipulation in Python 
	rather than Java.
'''

import unittest

def solve_iter(n):
	n = [i for i in n]
	for i in range(len(n)/2):
		tmp = n[i]
		n[i] = n[-1 - i]
		n[-1 - i] = tmp
	return ''.join(n)

def solve_recur(n):
	if len(n) <= 1:
		return n
	return solve_recur(n[1:]) + n[0]

class Test(unittest.TestCase):
	
	data = [('abcdefghi', 'ihgfedcba')]
	
	def test_solution(self):
		for [case, expected] in self.data:
			actual = solve_iter(case)
			self.assertEqual(actual, expected)
			actual = solve_recur(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
