import unittest

class Stack:

	def __init__(self):

		self.stack = []

	def push(self, value):
		self.stack.append(value)

	def pop(self):
		return self.stack.pop() if len(self.stack) > 0 else None


'''
	enqueue - Runs in O(n) time
	dequeue - Runs in O(1) time
'''
class StackQueue:

	def __init__(self):
		self.queue = Stack()
		self.skele = Stack()

	def enqueue(self, value):
		element = self.queue.pop()
		while element is not None:
			self.skele.push(element)
			element = self.queue.pop()
		self.queue.push(value)
		
		element = self.skele.pop()
		while element is not None:
			self.queue.push(element)
			element = self.skele.pop()
		
	def dequeue(self):
		return self.queue.pop()

def solve(enqueue, dequeue_count):
	queue = StackQueue()
	for elm in enqueue:
		queue.enqueue(elm)
	dequeued = []
	for i in range(dequeue_count):
		dequeued.append(queue.dequeue())
	return dequeued

class Test(unittest.TestCase):

	data = [(([10,5,11,4,3,6,1], 5), [10, 5, 11, 4, 3])]

	def test(self):
		for case, expected in self.data:
			actual = solve(case[0], case[1])
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
		
