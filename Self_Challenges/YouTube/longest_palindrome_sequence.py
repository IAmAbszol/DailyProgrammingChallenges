import unittest

def solve(arr):
	'''
	2	a	b	a	x	a	b	a	x
		0	1	2	3	4	5	6	7
	0	T	F	T	F	F	F	T	F
	1		T	F	F	F	T	F	F
	2			T	F	T	F	F	F
	3				T	F	F	F	T
	4					T	F	T	F
	5						T	F	F
	6							T	F
	7								T
	'''
	if arr is None:
		return arr
	table = [[False if i != j else True for i in range(len(arr))] for j in range(len(arr))]
	best = 1
	for l in range(2, len(arr) + 1):
		palindrome = 0
		for i in range(0, len(arr) - l + 1):
			j = i + l - 1
			palindrome = 0
			if l == 2:
				if arr[i] == arr[j]:
					table[i][j] = True
					if i == 0 and j >= len(arr) - 1:
						palindrome = 2
			else:
				if arr[i] == arr[j] and table[i + 1][j - 1]:
					table[i][j] = True
					palindrome = j - i + 1
			if palindrome > best:
				best = palindrome
	return best

class Test(unittest.TestCase):

	data = [(['a','b','a','x','a','b','a','x'], 7),
			(['a','a'], 2)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
