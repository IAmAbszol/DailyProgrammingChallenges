'''
	LCA of a BT.

							3
				6					8
		2			9					13
				11		5			7

	2,5 -> 6
	2,11 -> 6
	8,11 -> 3
	8,7 -> 8

	Procedure: Construct a DFS approach from root to leaf.
	Base Case: If leaf, return null to parent if not value else return value.
	If value currently on is value needed, return value. 
	(This is case 4 on 8,7, no matter what, our first found value will be a lca to the next)
	Traverse left
	Record left
	Traverse right
	Record right
	If both are null, return null to parent.
	Else return value. If both contain values, this is our LCA, return our value else 
	return the non-null value.
'''

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def problem(root, values):
	if root is None:
		return None
	if not root.left and not root.right:
		if root.value in values:
			return root.value
		else:
			return None
	
	left_value = problem(root.left, values)
	right_value = problem(root.right, values)
	our_value = root.value

	if our_value in values:
		return our_value

	if left_value is not None and right_value is not None:
		return our_value
	if left_value is None and right_value is not None:
		return right_value
	else:
		return left_value

root = Node(3, left=Node(6, left=Node(2), right=Node(9, left=Node(11), right=Node(5))), right=Node(8, right=Node(13, left=Node(7))))

print(problem(root, [8,7]))
