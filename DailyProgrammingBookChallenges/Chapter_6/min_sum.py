from collections import defaultdict, deque

# Extremely close to my example, contain tuples inside queue to proceed.
class Node:

	def __init__(self, val, left=None, right=None):
		self.value = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.value)

def minimum(root):
	if root is None:
		return None

	queue = deque([])
	queue.append((root, 0))

	level = defaultdict(int)

	while queue:
		node, node_level = queue.popleft()
		
		level[node_level] += node.value

		if node.left:
			queue.append((node.left, node_level + 1))

		if node.right:
			queue.append((node.right, node_level + 1))
	return min(level, key=level.get)

root = Node(5, left=Node(1))
print(minimum(root))
