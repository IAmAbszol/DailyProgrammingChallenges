'''
	Algorithm works on both a BST and a regular Binary Tree.
'''

from queue import Queue
from copy import deepcopy

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def dist(root, a, b):
	if root is None:
		return root

	start = end = None
	tree_queue = Queue()
	if root.value == a:
		start = 0
	elif root.value == b:
		end = 0

	tree_queue.put((root, 0, []))
	while not tree_queue.empty():
		node, dist, path = tree_queue.get()
		if node.value == a:
			start = (dist, path)
		elif node.value == b:
			end = (dist, path)
		if start is not None and end is not None:
			if start[1][0] == end[1][0]:
				print(a,b)
				return max(start[0], end[0]) - min(start[0], end[0])
			return start[0] + end[0]
		if node.left is not None:
			copied = deepcopy(path)
			copied.append('L')
			tree_queue.put((node.left, dist + 1, copied))
		if node.right is not None:
			copied = deepcopy(path)
			copied.append('R')
			tree_queue.put((node.right, dist + 1, copied))

	return None

print(dist(Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6, right=Node(8)), right=Node(7))), 4, 5))
print(dist(Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6, right=Node(8)), right=Node(7))), 4, 6))
print(dist(Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6, right=Node(8)), right=Node(7))), 3, 4))
print(dist(Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6, right=Node(8)), right=Node(7))), 2, 4))
print(dist(Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6, right=Node(8)), right=Node(7))), 8, 5))
print(dist(Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6, right=Node(8)), right=Node(7))), 3, 8))
