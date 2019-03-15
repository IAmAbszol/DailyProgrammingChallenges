from copy import deepcopy

class Node:

	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node

	def __str__(self):
		return str(self.value)

class LinkedList:

	def __init__(self):
		self.head = None

	def insert(self, value):
		node = Node(value)
		node.next_node = self.head
		self.head = node

	def print_list(self):
		tmp = deepcopy(self.head)
		while tmp is not None:
			print(tmp)
			tmp = tmp.next_node

def add(node1, node2, carry=0):
	
	'''
		9 -> 9 = 99
		5 -> 2 = 25

		124 --> 4 -> 2 -> 1
		
		4, next_node=add(node1.next_node, node2.next_node, carry=1)
		
		9 + 2 + 1 = 12
		12 % 10 == 1
		2, next_node=add(node1.next_node, node2.next_node, carry=1)
	'''

	if node1 is None and node2 is None and not carry:
		return None

	node1_val = node1.value if node1 else 0
	node2_val = node2.value if node2 else 0
	total = node1_val + node2_val + carry

	node1_next = node1.next_node if node1 else None
	node2_next = node2.next_node if node2 else None

	return Node(total % 10, next_node=add(node1_next, node2_next, carry=1 if total >= 10 else 0))

nine = Node(9, next_node=Node(9))

five = Node(5, next_node=Node(2))

added = add(nine, five)
print(added.value)
print(added.next_node.value)
print(added.next_node.next_node.value)

