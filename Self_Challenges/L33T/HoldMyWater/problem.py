import unittest

'''
	O(n), best
'''
def solve(arr):

	if arr is None: 
		return arr

	absolute_max = 0
	i, j = 0, 1
	while i <= j and j < len(arr):
		absolute_max = max((j - i) * min(arr[i], arr[j]), absolute_max)
		if arr[i] < arr[j]:
			i += 1
		else:
			j += 1		
	return absolute_max


'''
	O(n^2) Naive
def solve(arr):
	
	if arr is None:
		return arr

	absolute_max = 0
	for i in range(len(arr)):
		cur_max = 0
		for j in range(i, len(arr)):
			tmp = (j - i) * min(arr[i], arr[j])
			if tmp > cur_max:
				cur_max = tmp
		if cur_max > absolute_max:
			absolute_max = cur_max
	return absolute_max
'''
class Test(unittest.TestCase):
	
	data =[([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
