import unittest

def solve(case):
	print(case)
	symbols = ['(', '[', '{', ')', ']', '}']
	stack = []
	for i in range(len(case)):
		if case[i] in symbols:
			symbol_index = symbols.index(case[i])
			if symbol_index < (len(symbols) / 2):
				stack.append(case[i])
			elif symbol_index >= (len(symbols) / 2):
				elm = stack.pop()
				if (symbol_index - len(symbols) / 2) != symbols.index(elm):
					return False
	if stack:
		return False
	return True
	

class Tests(unittest.TestCase):

	data = [('(())[]{}', True), ('[{()}}', False), ('[(){}}', False), ('[()[]]', True)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()	
