class Node:

	def __init__(self, val, left=None, right=None):
		self.value = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.value)

def array_to_bst(arr):
	# Usually I do `is not None` but we might run into the case of mere empty =/ None
	if not arr:
		return arr
	
	mid = arr // 2
	
	node = Node(arr[mid])
	node.left = array_to_bst(arr[:mid])
	node.right = array_to_bst(arr[mid + 1:])
	
	return node
