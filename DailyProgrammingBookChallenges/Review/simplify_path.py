import unittest

'''
	This problem can be broken down into
	either a directory or ..
	A directory signifies a push
	A .. signifies a pop
	Obvious stack use.
'''
def simplify(path):
	stack = []
	components = path.split('/')
	for component in components:
		if component.isalpha():
			stack.append(component)
		elif component == '..':
			if stack:
				stack.pop()
	simplified_path = '/'
	for idx, element in enumerate(stack):
		simplified_path += '{}'.format(element)
		if len(stack) - 1 != idx:
			simplified_path += '/'
	return simplified_path

class Test(unittest.TestCase):
	
	data = [('/home/', '/home'),
			('/../', '/'),
			('/home//foo/', '/home/foo'),
			('/a/../../b/../c//.//', '/c'),
			('/a//b////c/d//././/..', '/a/b/c')]

	def test(self):
		for case, expected in self.data:
			actual = simplify(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
