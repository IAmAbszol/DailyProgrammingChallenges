import unittest

def solve(arr):
	if arr is None:
		return arr
	count = 0
	for elm in arr:
		count += elm
		if count < 0:
			count = 0
	return count

class Test(unittest.TestCase):
	
	data = [([34,-50,42,14,-5,86], 137),
			([-5,-1,-8,-9], 0)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
