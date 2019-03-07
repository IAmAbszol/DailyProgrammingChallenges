import unittest

def solve(n):
	'''
		n = 4
		ret = 46
		--> ret = 4 * 10 + (10 - 4)

		n = 44
		ret = 442
		--> ret = 44 * 10 + (10 - 8)
		n = 56
		ret = -156
		-1 --> 100
		+ n --> 56 = 156 --> -156
	'''	
	if n < 0:
		return None
	n_sep = [int(i) for i in str(n)]
	if sum(n_sep) >= 10:
		val = abs((10 - sum(n_sep)) * 10 ** len(n_sep))
		return -(val + n)
	return (n * 10) + (10 - sum(n_sep))

class Test(unittest.TestCase):

	data = [(11, 118),
			(12, 127),
			(123, 1234),
			(56, -156),
			(77, -477)]
	
	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
