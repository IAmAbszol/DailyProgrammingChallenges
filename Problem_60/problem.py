import unittest

def solve(arr):
	if arr is None:
		return None

	arr.sort()
	ptr_l = 0
	ptr_r = len(arr) - 1
	subset_sum = False
	while ptr_l < ptr_r:
		lhs = sum([v for v in arr[:(ptr_l + 1)]])
		rhs = sum([v for v in arr[ptr_r:]])
		if lhs < rhs:
			ptr_l += 1
			subset_sum = False
		elif lhs > rhs:
			ptr_r -= 1
			subset_sum = False
		else:
			ptr_l += 1
			ptr_r -= 1
			subset_sum = True
	return subset_sum

class Test(unittest.TestCase):
	
	data = [([15,5,20,10,35,15,10], True),
			([15,5,20,10,35], False)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
