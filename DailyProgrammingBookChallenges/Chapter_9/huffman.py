import heapq

class Node:

	def __init__(self, char, left=None, right=None):
		self.char = char
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.char)

def building_huffman(frequencies):
	if frequencies is None:
		return None
	nodes = []

	for char, freq in frequencies.items():
		heapq.heappush(nodes, (freq, Node(char)))

	while len(nodes) > 1:
		freq1, node1 = heapq.heappop(nodes)
		freq2, node2 = heapq.heappop(nodes)

		heapq.heappush(nodes, (freq1 + freq2, Node('*', left=node1, right=node2)))

	return nodes[0][1]


def encode(root, string='', mapping={}):
	if not root:
		return

	if not root.left and not root.right:
		mapping[root.char] = string

	encode(root.left, string + '0', mapping)
	encode(root.right, string + '1', mapping)

	return mapping


def print_tree(root):
	from queue import Queue
	if root is None:
		return
	b = Queue()
	b.put(root)
	while not b.empty():
		nodes = []
		while not b.empty():
			node = b.get()
			print(node.char, end='')
			if node.left:
				nodes.append(node.left)
			if node.right:
				nodes.append(node.right)
		print()
		for node in nodes:
			b.put(node)
		
	
frequencies = {'a':3,'c':6,'e':8,'f':2}
print(building_huffman(frequencies))
root = (building_huffman(frequencies))
print_tree(root)
print(encode(root))
