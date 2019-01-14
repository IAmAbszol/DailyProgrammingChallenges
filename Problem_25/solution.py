'''
	solution.py
	Extremely similar to the island problem, 
	this time it's number of steps.
'''

import unittest

def solve(case):
	return f_regex(case[0], case[1], 0, 0)

def f_regex(str, regex, i, j):
	'''	
		Parameters
		----------
		str : String of which the regex will be applied too.
		regex : String containing *, . or any type of character to match.
		i : Index of traversing String.
		j : Index of traversing Regular Expression.

		Return
		----------
		boolean True if found, else False
	'''
	print(str, regex, " i : {}, j {}".format(i, j), str[i], regex[j])
	if j == len(regex):
		return True
	# Exhuastive, better implementation later would be to test 
	# the ending characters of Regex, does it even matter to test?
	if i == len(str):
		return False
	if str[i] != regex[j]:
		if regex[j] == '.':
			return f_regex(str, regex, i + 1, j + 1)
		if regex[j] == '*':
			# Remove * for analysis
			spliced_regex = regex[j:].replace("*", "")
			for x in range(0, len(str) - regex.count('*')):
				if f_regex(str, spliced_regex, i + x, 0):
					return True
		return False
	if str[i] == regex[j]:
		return f_regex(str, regex, i + 1, j + 1)

	return False
	

class Test(unittest.TestCase):
	'''	
	data = [(("Hello", "*llo"), True),
			(("Hello", ".llo"), False),
			(("Hello", "*.l."), False),
			(("Hello", "*.llo"), True)]	
	'''
	data = [(("Hello", "*ll"), False)]
	def test_solution(self):
		for [case, expected] in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
