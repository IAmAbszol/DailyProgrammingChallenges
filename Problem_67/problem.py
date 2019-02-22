import gc

from copy import deepcopy

'''

	3
	1, 2, 3 --> Appends
	4,2,5

	dict = {}
	1 --> Node
	2 --> Node
	3 --> Node

	--> value
	
	get(key)
		if not key in self.cache.keys()
			return None	
		node = self.cache[key]
		self.cache_list.delete(node)
		self.append(node)
		return node.value

'''		

class Node:

	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

class DoublyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def append(self, value):
		node = Node(value)
		node.prev = self.tail
		if self.tail is not None:
			self.tail.next = node
		if self.head is None:
			self.head = self.tail
		self.tail = node
		self.size += 1
		return node

	def delete(self, node):
		if node is None:
			return None
		if self.head == node:
			self.head = node.next
		if self.tail == node:
			self.tail = node.prev
		if node.next is not None:
			node.next.prev = node.prev
		if node.prev is not None:
			node.prev.next = node.next
		gc.collect()
		self.size -= 1
		return node

	def __str__(self):
		traverse = deepcopy(self.head)
		string = ''
		while traverse.next is not None:
			string += '{}, '.format(traverse.value)
			traverse = traverse.next
		string += str(traverse.value)
		return string

class LFU:

	def __init__(self, cache_size):
		self.cache = {}
		self.cache_list = DoublyLinkedList()
		self.size = cache_size

	'''
		Bug! - cache never pops dead keys
	'''
	def set(self, key, val):
		if self.cache_list.size >= self.size:
			node = self.cache_list.delete(self.cache_list.head)
			# Retrieval can occur in O(1), discard is O(n)
			key = None
			for k, v in self.cache.items():
				if v == node:
					key = k
			if key is not None:
				self.cache.pop(key)
		if key in self.cache.keys():
			self.cache_list.delete(self.cache[key])
		node = self.cache_list.append(val)
		self.cache[key] = node

	def get(self, key):
		node = self.cache[key]
		self.cache_list.delete(node)
		self.cache_list.append(node.value)
		return node.value


lfu = LFU(3)
lfu.set('a', 1)
lfu.set('b', 2)
lfu.set('c', 3)
lfu.set('d', 4)
lfu.get('c')
lfu.get('b')
lfu.set('e', 10)
print(lfu.cache_list)