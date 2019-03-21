'''
	Algorithm for this problem can be summarized as using a post-order traversal
	and a Kadane's algorithm implementation.

			10
		5		20
	1		4 -5	50

	If we ran through this we would find by using the all mighty oracle would say
	4 -> 5 -> 10 -> 20 -> 50

	Post order traversal has us obtain 1 first and we will compare to ending and overall current.
'''

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def solution(root):
	if root is None:
		return 0, 0

	l_current, l_top = solution(root.left)
	r_current, r_top = solution(root.right)

	current_max = max(max(l_current, r_current) + root.value, root.value)
	
	top = max(current_max, l_current + r_current + root.value)

	total = max(l_top, r_top, top)
	return current_max, total

root = Node(10, left=Node(5, left=Node(1), right=Node(4)), right=Node(20, left=Node(-5), right=Node(50)))
print(solution(root)[1])
