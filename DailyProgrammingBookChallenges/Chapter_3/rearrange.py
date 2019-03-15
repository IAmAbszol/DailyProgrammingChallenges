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

	def rearrange(self):
		'''
			1 2 3 4 5
			cur.data, cur.next.data = cur.next.value, cur.data
		'''

		even = True
		cur = self.head
		
		while cur.next_node is not None:

			if cur.value > cur.next_node.value and even:
				cur.value, cur.next_node.value = cur.next_node.value, cur.value

			if cur.value < cur.next_node.value and not even:
				cur.value, cur.next_node.value = cur.next_node.value, cur.value

			even = not even
			cur = cur.next_node

ls = LinkedList()
ls.insert(5)
ls.insert(4)
ls.insert(3)
ls.insert(2)
ls.insert(1)

ls.print_list()
ls.rearrange()
ls.print_list()


