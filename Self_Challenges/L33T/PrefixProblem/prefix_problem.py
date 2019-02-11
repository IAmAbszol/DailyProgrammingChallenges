import unittest

def solve(arr):
	if arr is None:
		return arr
	prefix = ''
	minimum = min(arr)
	for idx, c in enumerate(minimum):
		for elm in arr:
			if elm[idx] != c:
				return prefix
		prefix += c
	return prefix
		


class Test(unittest.TestCase):

	data = [(['leet', 'leetcode', 'le'], 'le')]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
