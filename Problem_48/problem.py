import unittest

class Node:

	def __init__(self, value, left=None, right=None):
		self.right = right
		self.left = left
		self.value = value


def solve(arr):
	if arr is None:
		return arr
	preorder = arr[0]
	inorder = arr[1]
	if len(preorder) != len(inorder):
		return None
	if len(preorder) == len(inorder) == 1:
		return preorder[0]
	node = Node(preorder[0])
	index = inorder.index(preorder[0])
	node.left = solve((preorder[1:index+1], inorder[0:index]))
	node.right = solve((preorder[index + 1:], inorder[index+1:]))
	return node


class Test(unittest.TestCase):

	data = [((['a','b','d','e','c','f','g'],['d','b','e','a','f','c','g']), [Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f'), Node('g')))])]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()	
