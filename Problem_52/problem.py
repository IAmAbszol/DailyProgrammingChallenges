import gc
from copy import deepcopy

'''
class LRU:

	def __init__(self, n):
		self.cache_size = n
		self.cache_list = []
		self.cache = {}

	def set(self, key, value):
		if len(self.cache_list) >= self.cache_size:
			k = self.cache_list.pop()
			self.cache.pop(k)
		if key in self.cache.keys():
			# Pop key from current position, add to start as most recently used
			self.cache_list.insert(0, self.cache_list.pop(self.cache_list.index(key)))
		else:
			self.cache_list.insert(0, key)
		self.cache[key] = value
	
	def get(self, key):
		if key not in self.cache.keys():
			return None
		# Get key index, place in front
		self.cache_list.insert(0, self.cache_list.pop(self.cache_list.index(key)))
		return self.cache[key]
'''

# Previous list is of O(n) and not have constant time, suggestion, doubly linked list
# Has contains key + address, doubly has address and value.
# Due to python's nature, we will hold the node inside the hash.
class Node:

	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

class Doubly:

	def __init__(self):
		self.head = None		
		self.last = None
		self.length = 0

	def insert(self, value):
		node = Node(value)
		node.next = self.head
		node.prev = None
		
		if self.head is not None:
			self.head.prev = node

		if self.last is None:
			self.last = self.head

		self.head = node
		self.length += 1
		return node

	def delete(self, node):
		if node is None or self.head is None or self.last is None:
			return None
		if self.head == node:
			self.head = node.next
		if self.last == node:
			self.last = node.prev
		# Set the next one's previous to the one before this node.
		if node.next is not None:
			node.next.prev = node.prev
		# Set the previous one's next to the one before this node
		if node.prev is not None:
			node.prev.next = node.next
		gc.collect()
		self.length -= 1


	def print_list(self):
		node = deepcopy(self.head)
		while node is not None:
			print(node.value)
			node = node.next

class LRU:

	def __init__(self, n):
		self.cache_size = n
		self.lru_list = Doubly()
		self.cache = {}

	def set(self, key, value):
		# Last element is the one least recently used
		if self.lru_list.length >= self.cache_size:
			self.lru_list.delete(self.lru_list.last)
		if key in self.cache.keys():
			self.lru_list.delete(self.cache[key])
		node = self.lru_list.insert(value)
		self.cache[key] = node

	def get(self, key):
		retrieved_node = self.cache[key]
		self.lru_list.delete(retrieved_node)
		# Place it back into list, this one will become head
		self.lru_list.insert(retrieved_node.value)
		return retrieved_node.value

lru = LRU(2)
for i in range(4):
	lru.set(i, i*10)
print(lru.get(2))
print("--------")
lru.lru_list.print_list()
lru.set('a', 100)
print("--------")
lru.lru_list.print_list()
