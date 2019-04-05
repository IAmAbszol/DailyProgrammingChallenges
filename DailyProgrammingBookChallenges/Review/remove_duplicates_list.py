from copy import deepcopy

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class SinglyLinkedList:

	def __init__(self):
		self.head = None

	def append(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
			return
		traverse = self.head
		while traverse.right is not None:
			traverse = traverse.right
		traverse.right = node
	
	def print(self):
		node = self.head
		while node is not None:
			print(node.value)
			node = node.right

def problem(head):
	removed = Node(None)
	cur = head
	pre = removed
	while cur is not None:
		while cur.right is not None and cur.value == cur.right.value:
			cur = cur.right
		if pre.right == cur:
			pre = cur
		else:
			pre.right = cur.right
		cur = cur.right
	return removed.right

dupes = SinglyLinkedList()
my_list = [1,1,1,2,3,4,4,5]
for element in my_list:
	dupes.append(element)
dupes.print()

removed = problem(dupes.head)
dupes.head = removed
dupes.print()
