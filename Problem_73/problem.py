from copy import deepcopy

class Node:

	def __init__(self, val, next_node=None):
		self.value = val
		self.next_node = next_node

	def __str__(self):
		return 'Node {} points to {}.'.format(self.value, id(self.next_node))

class SinglyLinkedList:

	def __init__(self):
		self.head = None

	def insert(self, node):
		if self.head is None:
			self.head = node
			return
		node.next_node = self.head
		self.head = node
		return

	def reverse(self):
		'''
			14 10 1
			^
			14 -> None
			10 -> 14 -> None
			1 -> 10 -> 14 -> None
			^
		'''
		_next, _current = None, self.head
		while _current is not None:
			tmp = _current.next_node
			_current.next_node = _next
			_next = _current
			_current = tmp
		self.head = _next

	def __str__(self):
		node_list = []
		head_ptr = deepcopy(self.head)
		while head_ptr is not None:
			node_list.append(head_ptr.value)
			head_ptr = head_ptr.next_node
		return str(node_list)

one = Node(1)
ten = Node(10)
fourteen = Node(14)

singlylinked = SinglyLinkedList()
singlylinked.insert(one)
singlylinked.insert(ten)
singlylinked.insert(fourteen)

print(singlylinked)

singlylinked.reverse()

print(singlylinked)
