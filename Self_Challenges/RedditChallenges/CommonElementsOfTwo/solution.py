'''
	solution.py
	Decided to do this in Python, since it appeals
	to perform list/array manipulation in Python 
	rather than Java.
'''

import unittest

def solve(arrs):
	commons = []
	for i in arrs[0]:
		if i in arrs[1]:
			commons.append(i)
	return list(set(commons))

class Test(unittest.TestCase):
	
	data = [(([9,8,1,4,0,2],[14,7,6,3,3,2,5,0,10,11,1]), [0,1,2]),
			(([0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]), [])]
	
	
	def test_solution(self):
		for [case, expected] in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
