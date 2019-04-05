from queue import Queue

class Node:
	
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def problem(root):
	
	if root is None:
		return root

	tree = Queue()
	tree.put(root)
	while not tree.empty():
		node = tree.get()
		print(node.value)
		if node.left:
			tree.put(node.left)
		if node.right:
			tree.put(node.right)

root = Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))
problem(root)
