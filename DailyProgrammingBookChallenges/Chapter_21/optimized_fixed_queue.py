class FixedQueue:

	def __init__(self, size):
		self.queue_size = size
		self.queue = [[]]
		self.head_ptr = 0	
		self.tail_ptr = 0
		self.tail_array = 0
		self.current_size = 0

	def enqueue(self, value):
		self.queue[self.tail_array].append(value)
		if len(self.queue[self.tail_array]) == self.queue_size:
			self.queue.append([])
			self.tail_array += 1
		self.tail_ptr += 1
		self.current_size += 1	

	def dequeue(self):
		if self.current_size == 0:
			raise 'Queue is empty'
			return
		value = self.queue[self.head_array][self.head_ptr]
		self.head_ptr += 1
		if self.head_ptr >= self.queue_size:
			self.head_ptr = 0
			del self.queue[head_array]
			self.tail_array -= 1
		self.current_size -= 1
		return value 

	def get_size(self):
		return self.current_size
