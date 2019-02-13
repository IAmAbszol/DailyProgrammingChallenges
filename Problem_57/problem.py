import unittest

def solve(arr, k):
	if arr is None or len(arr) == 1:
		return arr
	if k < 1:
		return None
	processed = []
	start, mid, end = None, None, None
	for idx, elm in enumerate(arr):
		if elm.isalpha() and mid is None:
			mid = idx
			if elm.isalpha() and start is None:
				start = idx
		if elm == ' ':
			end = idx
			mid = None
		if idx - start == k:
			processed.append(arr[start:end])
			start = mid
			mid = None
			end = None
	if end is None:
		processed.append(arr[start:len(arr)])
	return processed	

class Test(unittest.TestCase):
	
	data = [(('the quick brown fox jumps over the lazy dog', 10), ['the quick', 'brown fox', 'jumps over', 'the lazy', 'dog'])]
	
	def test(self):
		for case, expected in self.data:
			actual = solve(case[0], case[1])
			self.assertEquals(actual, expected)

if __name__ == '__main__':
#	unittest.main()
	data = [(('the quick brown fox jumps over the lazy dog', 10), ['the quick', 'brown fox', 'jumps over', 'the lazy', 'dog'])]
	print(solve(data[0][0][0], data[0][0][1]))
