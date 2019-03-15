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

	def reverse_list(self):
		'''
			5 4 3 2 1
			cur
			prev
			cur = 4
			prev = 5

			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
			
			
		'''

		# For WHATEVER REASON my old solution wasn't working. Literally only changed
		# variable names =/	
		_next, _current = None, self.head
		while _current is not None:
			tmp = _current.next_node
			_current.next_node = _next
			_next = _current
			_current = tmp
		self.head = _next
		
l = LinkedList()
l.insert(1)
l.insert(5)
l.insert(10)
l.reverse_list()
l.print_list()










