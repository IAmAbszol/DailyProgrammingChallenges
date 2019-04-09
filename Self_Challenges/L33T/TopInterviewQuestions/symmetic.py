'''
	[1,2,2,3,4,4,3,		1,2,2,1,1,2,2,1]
			1
		2		2
	3	  4	  4		3
1	  2	 2	1 1	2 2		1
	T

	Originally was doing it array based as it goes by power of 2.

	Get the offset + i == (offset + reach - i) to compare
	symmetry.

'''

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def symmetric(root):
		
	def traverse(a, b):
		if a is None and b is None:
			return True
		if a is None or b is None:
			return False
		if a.value != b.value:
			return False
		return traverse(a.left, b.right) and traverse(a.right, b.left)
	
	return traverse(root.left, root.right)

root = Node(1, left=Node(3, left=Node(3), right=Node(4)), right=Node(2, left=Node(4), right=Node(3)))
print(symmetric(root))


