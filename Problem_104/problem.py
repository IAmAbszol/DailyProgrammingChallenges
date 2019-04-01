'''
	Linked list problem of being a palindrome

	Case doubly linked list:
	1 -> 4 -> 3 -> 4 -> 1
	^ 					^
	Head				Tail
	If head == trail, head.next, tail.prev

	Case singly linked list:
	1 -> 4 -> 3 -> 3 -> 1

	Either O(n^2) time complexity with constant space or make a 
	new copy of the singly linked list by reversing it.
	Compare from pos 0 of each, any difference causes a no palindrome flag.
	O(n) time, O(n) space
'''

from copy import deepcopy

class Node: 

	def __init__(self, value, nextNode=None, prevNode=None):
		self.value = int(value)
		self.next = nextNode
		self.prev = prevNode

	def __str__(self):
		return str(self.value)

class DoublyLinkedList:

	def __init__(self, append_list):
		self.head = None
		self.tail = None
		for element in append_list:
			self.append(element)

	def append(self, value):
		node = Node(value)
		if self.head is None and self.tail is None:
			self.head = self.tail = node
			return
		self.tail.prev = self.tail
		self.tail.prev.next = node
		self.tail = node

	def print(self):
		node = deepcopy(self.head)
		while node is not None:
			print(node)
			node = node.next

	def is_palindrome(self):
		if self.head is None:
			return False
		head_ptr = deepcopy(self.head)
		tail_ptr = deepcopy(self.tail)
		while head_ptr is not None and tail_ptr is not None:
			if head_ptr.value != tail_ptr.value:
				return False
			head_ptr = head_ptr.next
			tail_ptr = tail_ptr.prev
		return True

class SinglyLinkedList:
		
	def __init__(self, append_list):
		self.head = None
		for element in append_list:
			self.append(element)

	def append(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
			return
		traversal_node = self.head
		while traversal_node.next is not None:
			traversal_node = traversal_node.next
		traversal_node.next = node
	
	def print(self):
		node = deepcopy(self.head)
		while node is not None:
			print(node)
			node = node.next

	def is_palindrome(self):
		my_list = []
		node = deepcopy(self.head)
		while node is not None:
			my_list.insert(0, node.value)
			node = node.next
		node = deepcopy(self.head)
		for element in my_list:
			if element != node.value:
				return False
			node = node.next			
		return True

for ls in ([1,3,4,3,1],[2,2],[2],[5,4,3]):
	doubly = DoublyLinkedList(ls)
	singly = SinglyLinkedList(ls)
	print(doubly.is_palindrome())
	print(singly.is_palindrome())
	print("-"*50)
