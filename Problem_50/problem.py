import unittest

class Node:

	def __init__(self, value, left=None, right=None):
		self.left = left
		self.right = right
		self.value = unicode(str(value), 'utf-8')


def operand(operand, left, right):
	if operand == '+':
		return left + right
	elif operand == '-':
		return left - right
	elif operand == '*':
		return left * right
	elif operand == '/':
		return left / right


def solve(tree):
	if tree is None:
		return tree
	if tree.value.isnumeric():
		return int(tree.value)
	return operand(tree.value, solve(tree.left), solve(tree.right))


class Test(unittest.TestCase):

	data = [(Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5))), 45)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
