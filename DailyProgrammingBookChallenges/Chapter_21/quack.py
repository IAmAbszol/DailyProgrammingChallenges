'''
	Don't fully understand why this data structure is so complex. Maybe
	coding it and visualizing the components will help me understand
	why we need to jump through so many hoops.
	* NVM, saw it said three STACKS!!!. This is damn near easy if it was an array
	
	Question like this might arise in a Queue using 2 stacks =O. Just keep rebalancing
	the stacks to obtain items for the queue operation

	S1
	S2
	Queue --> 1,2,3,4
	Pop --> 1
	Queue --> 5,6
	S1 --> 1,2,3,4
	Reverse stack to S2, pop. Mark S2 as dequeue stack now.
	Queue, reverse stack to S1, push. Mark S1 as enqueue stack now.
'''

class Quack:

	def __init__(self):
		self.left = []
		self.right = []
		self.buffer = []

	def push(self, value):
		self.left.append(value)

	def pop(self):
		if not self.left and not self.right:
			raise 'Empty queues'
			return
		if not self.left:
			mid = len(self.right) // 2
			for i in range(mid):
				self.buffer.append(self.right.pop())

			while self.right:
				self.left.append(self.right.pop())

			while self.buffer:
				self.right.append(self.buffer.pop())

		return self.left.pop()

	def pull(self):
		if not self.left and not self.right:
			raise 'Empty queues'
			return
		if not self.right:
			mid = len(self.left) // 2
			for i in range(mid):
				self.buffer.append(self.left.pop())
			while self.left:
				self.right.append(self.left.pop())
			while self.buffer:
				self.left.append(self.buffer.pop())
		return self.right.pop()
