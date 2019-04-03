import unittest

def cached_solution(arr):
	prev = 0
	for i in range(len(arr) - 1):
		prev += arr[i]
		if prev <= 0:
			return False
		prev -= 1
	return True

class Test(unittest.TestCase):
	
	data = [([2,2,3,0,0,0], True), ([1,0,1,0], False), ([2,0,1,0], True), ([2,1,0,0,0,0], False)]

	def test(self):
		for case, expected in self.data:
			actual = cached_solution(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
