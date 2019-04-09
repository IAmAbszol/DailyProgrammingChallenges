'''
		-10
	9		20
		15		7

	For this problem, we will first recursively move down the tree till root is None.
	
	Then we will bounce back to caller parent with the values of 0,0 (If it was none).
	Left is the current, right is the absolute maximum per this sub traversal.

	Next current will be calculated by taking the max
	of either left or right paired with our value or just our value.

	Top or absolute max is found by the max of our current combiend with left, right and root.value.

	We then return current and max of left_max, right_max, and absolute_max.
'''

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def problem(root):
	if root is None:
		return 0, 0

	left_curr, left_max = problem(root.left)
	right_curr, right_max = problem(root.right)

	curr = max(max(left_curr, right_curr) + root.value, root.value)
	absolute_max = max(left_curr+right+curr+root.value, curr)
	# The reason we don't evaluate the maxes are that a max can exist
	# deep within the tree and this might be our original parent caller. (-10)
	return curr, max(left_max, right_max, absolute_max)


