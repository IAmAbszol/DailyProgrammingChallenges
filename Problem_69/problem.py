import unittest

def solve(arr):
	
	summed = 0
	for i in range(len(arr) - 2):
		j = i + 1
		for z in range(j + 1, len(arr)): 
			summed = max(summed, arr[i] * arr[j] * arr[z])
	return summed

class Test(unittest.TestCase):

	data = [([-10,-10,2,5,3], 500),
			([-1,-2,-3,-4,10,9], 120)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
		
