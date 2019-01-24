import unittest

'''
	O(n*m) time complexity
	O(1) space complexity
'''
def solve(str1, str2):
	longest, shortest = (str1, str2) if len(str1) > len(str2) else (str1, str1)
	
	# Preprocess string
	sim_count = 0
	for i, l in enumerate(longest):
		count = 0
		for j, s in enumerate(shortest):
			if (i + j) >= len(longest):
				break
			if longest[i + j] == shortest[j]:
				count += 1
		if sim_count < count:
			sim_count = count
	return len(longest) - sim_count

class Test(unittest.TestCase):
	
	data = [(("sitting", "kitten"), 3),
			(("fandangle", "dan"), 6)]
	
	def test(self):
		for case, expected in self.data:
			actual = solve(case[0], case[1])
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
