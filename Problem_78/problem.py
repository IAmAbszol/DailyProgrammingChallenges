from copy import deepcopy

class Node:

	def __init__(self, value, next_node=None):
		self.value = str(value)
		self.next_node = next_node

	def __str__(self):
		return str(self.value)

class SinglyLinkedList:

	def __init__(self):
		self.head = None
		self.size = 0	

	def insert(self, node):
		if self.head is None:
			self.head = node
		else:
			node.next_node = self.head
			self.head = node
		self.size += 1	

	# O(n) time
	def append(self, node):
		if self.head is None:
			self.head = node
		else:
			tmp = self.head
			while tmp.next_node is not None:
				tmp = tmp.next_node
			tmp.next_node = node			
		self.size += 1

	def get(self, idx):
		if idx < 0:
			return None
		tmp = deepcopy(self.head)
		for i in range(idx):
			tmp = tmp.next_node
			if tmp is None:
				return None
		return tmp.value

	def __str__(self):
		my_list = []
		tmp = deepcopy(self.head)
		while tmp is not None:
			my_list.append(tmp.value)
			tmp = tmp.next_node
		return ','.join(my_list)

def merge_two(a, b):
	if a is None:
		return b
	if b is None:
		return a
	tmp = None
	if int(a.value) <= int(b.value):
		tmp = a
		tmp.next_node = merge_two(a.next_node, b)
	else:
		tmp = b
		tmp.next_node = merge_two(a, b.next_node)
	return tmp

def merge_singly(k):
	if k is None or not k:
		return None
	'''
		1 2
		4 5 9
		3 10

		1 2 4 5 9		

		3 10
	'''
	sorted_list = SinglyLinkedList()
	while len(k) > 1:
		tmp_k = []
		for i in range(len(k)):
			if (i + 1) % 2 == 0:
				sorted_nodes = merge_two(k[i].head, k[i - 1].head)
				tmp_list = SinglyLinkedList()
				tmp_list.head = sorted_nodes
				tmp_k.append(tmp_list)
				ptr = i + 1
		if ptr < len(k):
			tmp_k.append(k[-1])
		k = tmp_k
	sorted_list = k[0]	
	return sorted_list
		

single_one = SinglyLinkedList()
single_one.append(Node(1))
single_one.append(Node(2))

single_two = SinglyLinkedList()
single_two.append(Node(4))
single_two.append(Node(5))
single_two.append(Node(9))

single_three = SinglyLinkedList()
single_three.append(Node(3))
single_three.append(Node(10))

print(single_one)
print(single_two)
print(single_three)

sorted_list = merge_singly([single_one, single_two, single_three])
print(sorted_list)




	
