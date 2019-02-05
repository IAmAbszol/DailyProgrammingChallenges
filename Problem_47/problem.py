import unittest

'''
	O(n) time with constant space.
'''
def solve(arr):
	if arr is None:
		return arr
	price_best, profit_best = 0, 0
	for price in reversed(arr):
		price_best = max(price_best, price)
		profit = price_best - price
		profit_best = max(profit_best, profit)
	return profit_best


'''
	Naive way O(n^2)
def solve(arr):
	if arr is None:
		return arr
	best = 0
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			best = max(best, arr[j] - arr[i])
	return best
'''

class Test(unittest.TestCase):
	
	data = [([9, 11, 8, 5, 7, 10], 5)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
