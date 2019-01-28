'''
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

import unittest

def solve(arr):
	if arr is None:
		return arr
	arr_set_sum = sum(list(set(arr)))
	arr_sum = sum(arr)
	return ((3 * arr_set_sum) - arr_sum) / 2
	

class Test(unittest.TestCase):

	data=[([6,1,3,3,3,6,6], 1), 
		  ([13, 19, 13, 13], 19)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__=='__main__':
	unittest.main()
