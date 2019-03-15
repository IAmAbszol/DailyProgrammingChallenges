from copy import deepcopy

'''
	This script just looks at the values.
	A true intersection would look via the address or id() in Python.
	Simply modify the script without the LinkedList class and
	just look for when id(n1) == id(n2).
'''
class Node:

	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node

	def __str__(self):
		return str(self.value)

class LinkedList:

	def __init__(self):
		self.head = None
		self.length = 0	

	def insert(self, value):
		node = Node(value)
		node.next_node = self.head
		self.head = node
		self.length += 1

	def print_list(self):
		tmp = deepcopy(self.head)
		while tmp is not None:
			print(tmp)
			tmp = tmp.next_node


def intersecting(l1, l2):
	if l1 is None or l2 is None:
		return None

	l1_ptr = l1.head
	l2_ptr = l2.head

	# L1 has some nodes that don't coorespond with l2.
	if l1.length > l2.length:
		for i in range(l1.length - l2.length):
			l1_ptr = l1_ptr.next_node
	
	if l1.length < l2.length:
		for i in range(l2.length - l1.length):
			l2_ptr = l2_ptr.next_node

	# Read note above, basing on values but true would be on id.
	while l1_ptr.value != l2_ptr.value:
		l1_ptr = l1_ptr.next_node
		l2_ptr = l2_ptr.next_node

	return l1_ptr.value

l1 = LinkedList()
l2 = LinkedList()

l1.insert(10)
l1.insert(9)
l1.insert(8)
l1.insert(2)
l1.insert(1)

l2.insert(10)
l2.insert(9)
l2.insert(8)
l2.insert(4)

print(intersecting(l1, l2))
