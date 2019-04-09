'''
	Wanted to try instead of using Kadane's algorithm anywhere, what about on the leaves?
	Self challenge time.exe

			-20
		5			10
	3		2	5		9
				   	  0
				    4
	We should have a solution from the oracle as:
	5 -> 10 -> 9 -> 0 -> 4 = 28

	As 	
	3 -> 5 -> 2, 3 -> 5 -> -20 -> 5 are all bad.

	I'll proceed as in the previous but this time only calculate maxes by returning the data when we hit the end.
	This will force our algorithm to only look at leaves as it will be chained.
'''

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def max_sum(root):
	
	if root is None:
		return 0, 0

	# This will retrieve the value, notice how this is the only time we retrieve a leaf value instead of also considering
	# roots value, pretty much the main reason why this algorithm works.
	if root.left is None and root.right is None:
		return root.value, root.value

	# Traverse down the far left side, post-order traversal
	l_current, l_total = max_sum(root.left)
	r_current, r_total = max_sum(root.right)

	# If were not at these leaves, compute current max by considering if the left, the right, or the sum of them + root is the max
	if root.left is not None and root.right is not None:
		
		current_max = max(l_total, r_total, l_current + r_current + root.value)
		# Return either left or right and root.value, then the current max.
		return max(l_current, r_current) + root.value, current_max

	# If we have only one direction, either consider the maxes of the right + root and pass the r_total. Same with left
	if root.left is None:
		return r_current + root.value, r_total
	else:
		return l_current + root.value, l_total

root = Node(-20, left=Node(5, left=Node(3), right=Node(2)), right=Node(10, left=Node(5), right=Node(9, left=Node(0, left=Node(4)))))
print(max_sum(root)[1])
