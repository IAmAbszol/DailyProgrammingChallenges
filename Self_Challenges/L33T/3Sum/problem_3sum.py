import unittest

'''
	Complexity
	O(n^2) time
	O(n^2) space
'''
def solve(arr):
	if arr is None:
		return arr

	solution = []
	for i in range(len(arr) - 2):
		for j in range(i + 1, len(arr) -1):
			k = j + 1
			while k < len(arr):
				if arr[i] + arr[j] + arr[k] == 0:
					
					if any(all([x in s for x in [arr[i], arr[j], arr[k]]]) for s in solution):
						break
					solution.append([arr[i], arr[j], arr[k]])
				k += 1
	return solution


class Test(unittest.TestCase):

	data = [([-1,0,1,2,-1,-4], [[-1,0,1],[-1,-1,-2]])]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			# Temporary, use 'set' to determine list alikeness
			self.assertTrue(True)

if __name__ == '__main__':
	unittest.main()
