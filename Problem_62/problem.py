import unittest

def solve(m, n):
	if n < 0 or m < 0:
		return None
	# Build matrix
	matrix = [[0 for _ in range(n)] for _ in range(m)]
	# Fill out matrix
	# 1th n means we can only traverse m (Down)
	for i in range(m):
		matrix[i][0] = 1	
	# 1th m means we can only traverse n (Right)
	for i in range(n):
		matrix[0][i] = 1
	
	# Computation, take previous count column and row, sum.
	'''
		If we had
		0 0
		0 0
		Our matrix would be
		1 1
		1 0
		The 0 would say I could either go up or left (DP takes previous sub, hence this.)
		So 	
		1 + 1 = 2
		1 1
		1 2
		2 is our answer for the 2x2 matrix.
		TEST
		0 0 0 
		0 0 0 
		0 0 0
		------
		1 1 1
		1 2 3
		1 3 6
	'''
	for i in range(1, m):
		for j in range(1, n):
			matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
	return matrix[m - 1][n - 1]

class Test(unittest.TestCase):
	
	data = [((2,2), 2),
			((3,3), 6)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case[0], case[1])
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
