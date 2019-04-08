class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def count(n):

	def problem(i, j):
		if i >= j:
			return [None]
		if i == j:
			return [Node(i)]

		tree = []
		# Key of center
		for p in range(i, j + 1):
			# All lhs sub trees
			left = problem(i, p - 1)
			# All rhs sub trees
			right = problem(p + 1, j)
			for l in left:
				for r in right:
					# Build the trees!
					root = Node(p)
					root.left = l
					root.right = r
					tree.append(root)
		return tree
	return problem(1, n)

print(count(3))
