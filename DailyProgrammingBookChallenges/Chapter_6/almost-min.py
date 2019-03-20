import sys

from queue import Queue

class Node:

	def __init__(self, val, left=None, right=None):
		self.value = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.value)

'''
			1
		2		3
			4		5

	min_sum = 0
	
	level 0 = 1
	level 1 = 2
	level 2 = 4
	level 3 = 8
	Each iter = 2 ** i --> nodes to grab
	level = 0
	while not queue.isempty():
		
		current_sum = 0
		for i in range(2 ** level):
			current_sum += queue.pop().value
		if current_sum < min_sum:
			level = level
			min_sum = current_sum

	return level
'''

# Only works IF! each parent node has either no children or is full
def minimum(self, root):
	if root is None:
		return None

	sum_queue = Queue()
	sum_queue.put(root)

	min_level = 0
	min_sum = sys.maxsize
	
	current_level = 0

	while not sum_queue.isempty():
		
		current_sum = 0
		for i in range(2 ** current_level):
			node = sum_queue.pop()
			if node.left is not None and node.right is not None:
				sum_queue.put(node.left)
				sum_queue.put(node.right)
			current_sum += node.value
		if current_sum < min_sum:
			min_sum = current_sum
			min_level = current_level
		current_level += 1
	return min_level


