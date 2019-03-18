from queue import Queue

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		return str(value)

'''
	5
1		6
	2 7
	X

			10
		8		12
	5		9 11	13

Breadth, check left, check right to root value. If
rule breaks, return False
'''
def problem(root):
	if root is None:
		return False
	breadth = Queue()
	breadth.put(root)
	while not breadth.empty():
		root_value = breadth.get()
		if root_value.left is not None:
			if root_value.value < root_value.left.value:
				return False
			else:
				breadth.put(root_value.left)
		if root_value.right is not None:
			if root_value.value > root_value.right.value:
				return False
			else:
				breadth.put(root_value.right)
	return True

root = Node(5, left=Node(1, None, right=Node(2)), right=Node(6, left=Node(7)))
root2 = Node(10, left=Node(8, left=Node(5), right=Node(9)), right=Node(12, left=Node(11), right=Node(13)))

print(problem(root))
print(problem(root2))
