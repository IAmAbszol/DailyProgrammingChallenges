import unittest

def solve(a, b):
	if b < 0:
		return 0
	result = 1
	while b > 0:
		if b & 1:
			result *= a
		# Divide by 2, same as shifting right.
		b = b >> 1
		a *= a
	return result

class Test(unittest.TestCase):

	data = [((2,3), 8),
			((2,5), 32)]
	
	def test(self):
		for case, expected in self.data:
			actual = solve(case[0], case[1])
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
		
			
