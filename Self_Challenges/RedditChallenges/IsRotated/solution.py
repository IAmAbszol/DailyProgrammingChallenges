'''
	solution.py
	Decided to do this in Python, since it appeals
	to perform list/array manipulation in Python 
	rather than Java.
'''

import unittest

def isRotated(arrs):
	initial = arrs[0]
	rotated = arrs[1]
	# Take rotated and append it back onto the end
	rotated = rotated[:] + rotated[:]
	initial = ''.join([str(i) for i in initial])
	rotated = ''.join([str(i) for i in rotated])
	return initial in rotated

class Test(unittest.TestCase):
	
	data = [
	(([1,2,3,5,6,7,8], [5,6,7,8,1,2,3]), True),
	(([1,3,2,5,6,7,8], [2,5,6,7,8,3,1]), False)]
	
	
	def test_is_rotated(self):
		for [case, expected] in self.data:
			actual = isRotated(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
