import unittest

def display(two_d):
	for row in two_d:
		print(row)

def solve(arr, k):
	if arr is None:
		return arr
	arr.sort()
	# Create an arr by sum 
	memo = [[False for i in range(k + 1)] for j in range(len(arr))]
	
	# Set the 0th row as False except for its first value
	for col in range(len(memo[0])):
		memo[0][col] = True if col == arr[0] else False

	# Set 0th column as true
	for row in memo:
		row[0] = True

	# Solve 
	for row in range(1, len(memo)):
		for col in range(1, len(memo[row])):
			if col < arr[row]:
				memo[row][col] = memo[row - 1][col]
				continue
			memo[row][col] = memo[row - 1][col - arr[row]] if not memo[row - 1][col] else True

	# Reconstruct
	path = []
	i, j = len(memo) - 1, len(memo[0]) - 1
	while i > 0:
		if memo[i - 1][j]:
			i -= 1
			continue
		path.append(arr[i])
		j -= arr[i]
	# We still have some sum left over
	if j > 0:
		path.append(arr[0])
		
	return path

class Test(unittest.TestCase):

	data =[(([2,3,7,8,10], 18), [8, 7, 3]),
		   (([12,1,61,5,9,2], 24), [12,9,2,1])]

	def test(self):
		for case, expected in self.data:
			arr, k = case[0], case[1]
			actual = solve(arr, k)
			self.assertEquals(actual, expected)


if __name__== '__main__':
	unittest.main()
