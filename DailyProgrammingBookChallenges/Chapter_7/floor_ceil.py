class Node:

	def __init__(self, val, left=None, right=None):
		self.value = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.value)

def floor_ceil(root, x, floor=None, ceil=None):
	if root is None:
		return floor, ceil

	if x == root.value:
		return x, x
	elif x < root.value:
		floor, ceil = floor_ceil(root.left, x, floor, ceil=root.value)
	elif x > root.value:
		floor, ceil = floor_ceil(root.right, x, root.value, ceil=ceil)

	return floor, ceil


