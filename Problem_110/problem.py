class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def problem(root, result=[], stack=[]):
	if not root.left and not root.right:
		stack.append(root.value)
		result.append(stack[:])
		stack.pop()
		return
	stack.append(root.value)
	if root.left:
		problem(root.left, result, stack)
	if root.right:
		problem(root.right, result, stack)
	return result


