class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def serialize(root):
	if root is None:
		return '#'
	return "{} {} {}".format(root.val, serialize(root.left), serialize(root.right))
	
def deserialize(s):
	def helper():
		val = next(vals)
		if val is '#':
			return None
		node = Node(int(val))
		node.left = helper()
		node.right = helper()
		return node

	vals = iter(s.split())
	return helper()

node = Node('5', Node('2', Node('1')), Node('3'))

print("Serialized Tree")
print(serialize(node))

print("Deserialized Tree - Reconstructed")
print(serialize(deserialize(serialize(node))))
