import unittest
import math

from heapq import merge

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	middle = math.floor(len(arr) / 2)
	left = arr[:middle]
	right = arr[middle:]

	left = merge_sort(left)
	right = merge_sort(right)
	return list(merge(left, right))

def solve(arr):
	arr = merge_sort(arr)
	return max(arr[-3]*arr[-2]*arr[-1], arr[0] * arr[1] * arr[-1])

class Test(unittest.TestCase):

	data = [([-10,-10,2,5,3], 500),
			([-1,-2,-3,-4,10,9], 120)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
		
