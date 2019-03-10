import queue

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = str(value)
		self.left = left
		self.right = right

def print_tree(root):
	if root is None:
		return None
	print_queue = queue.Queue()
	print_queue.put(root)
	while not print_queue.empty():
		elm = print_queue.get()
		print(elm.value)
		if elm.left is not None:
			print_queue.put(elm.left)
		if elm.right is not None:
			print_queue.put(elm.right)

def print_by_level(root):
	if root is None:
		return None
	'''
	a
	b c
	d e f
	'''
	print_queue = queue.Queue()
	print_queue.put(root)
	while not print_queue.empty():
		next_level = []
		while not print_queue.empty():
			elm = print_queue.get()
			print(elm.value, end='')
			if elm.left is not None:
				next_level.append(elm.left)	
			if elm.right is not None:
				next_level.append(elm.right)
		for elm in next_level:
			print_queue.put(elm)
		print()

def inverse(root):
	if root is None:
		return None
	'''
			a
		b		c
	d		e f

			a
		c		b
			fd		e
	'''

	temp = root.left
	root.left = root.right
	root.right = temp
	inverse(root.left)
	inverse(root.right)

	return root

if __name__ == '__main__':
	root = Node('a', left=Node('b', left=Node('d'), right=Node('e')), 
					 right=Node('c', left=Node('f')))
	print_by_level(inverse(root))
	
