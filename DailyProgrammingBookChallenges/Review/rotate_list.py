class Node:

	def __init__(self, value, leftNode=None, rightNode=None):
		self.value = value
		self.left_node = leftNode
		self.right_node = rightNode

class SinglyLinkedList:

	def __init__(self):
		self.head = None
		self.length = 0

	def append(self, value):
		self.length += 1
		if self.head is None:
			self.head = Node(value)
			return
		tmp = self.head
		while tmp.right_node is not None:
			tmp = tmp.right_node
		tmp.right_node = Node(value)

	def print(self):
		tmp = self.head
		while tmp is not None:
			print(tmp.value)
			tmp = tmp.right_node
		print("-"*25)

	def rotate(self, k):
		if k < 1:
			return None
		'''
			Form a circular list
			1 2 3 4 5 -> 1 2 3 4 5, continually linked right.
			Traverse k times.
			Ending is now head.
			Set the prev next to None.
			Set head to node.
		'''
		# Find the end
		finding = self.head
		while finding.right_node is not None:
			finding = finding.right_node
		# Link the cycle
		finding.right_node = self.head
		# Iterate through k
		start = self.head
		prev = None
		for i in range(self.length - (k % self.length)):
			prev = start
			start = start.right_node
		prev.right_node = None
		self.head = start
		
	
my_list = [1,2,3,4,5]
singly = SinglyLinkedList()
for elm in my_list:
	singly.append(elm)
singly.print()
singly.rotate(2)
singly.print()
