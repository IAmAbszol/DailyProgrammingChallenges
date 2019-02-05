import unittest
# Manchester's algorithm is another implementation that runs in O(n) time using centers of palindromes's.
'''
	O(n^2) time and constant space
'''
def solve(s):
	if s is None:
		return s

	longest = ''
	low = high = 0
	for i in range(1, len(s)):
		low = i - 1
		high = i
		while low >= 0 and high < len(s) and s[low] == s[high]:
			if len(longest) < high - low + 1:
				longest = s[low:high+1]
			low -= 1
			high += 1
		low = i - 1
		high = i + 1
		while low >= 0 and high < len(s) and s[low] == s[high]:
			if len(longest) < high - low + 1:
				longest = s[low:high+1]
			low -= 1
			high += 1
	return longest

'''
	O(n^2) time and space
def solve(s):
	if s is None:
		return s

	longest = ''
	pals = [[False for i in range(len(s))] for j in range(len(s))]
	# Set single characters as true, as they are indeed palindromes
	for i in range(len(s)):
		pals[i][i] = True
	
	# Length 2?
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			pals[i][i + 1] = True
	
	# Now for the rest, start with k = 3
	for k in range(3, len(s) + 1):
		i = 0
		while i < (len(s) - k + 1):
			j = i + k - 1
			if pals[i + 1][j - 1] and s[i] == s[j]:
				pals[i][j] = True
				if len(longest) < k:
					longest = s[i:j + 1]
			i += 1
		
	return longest

	Naive way, O(n^3) complexity
def solve(s):
	if s is None:
		return s

	longest = ''
	for i in range(len(s)):
		for j in range(i, len(s)):
			a, b = i, j
			is_palindrome = True
			while a <= b:
				if s[a] != s[b]:
					is_palindrome = False
				a += 1
				b -= 1
			if is_palindrome:
				longest = s[i: j + 1] if len(longest) < len(s[i: j + 1]) else longest
	return longest
'''

class Test(unittest.TestCase):
	
	data = [('bananas', 'anana'),
			('racecar', 'racecar')]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)


if __name__ == '__main__':
	unittest.main()
