class FixedQueue:

	def __init(self, size):
		self.queue_size = size
		self.queue = [0 for _ in range(size)]
		self.head_ptr = 0
		self.tail_ptr = 0
		self.current_size = 0

	def enqueue(self, value):
		if current_size == queue_size:
			raise 'Queue is full'
			return
		queue_size[tail_ptr] = value
		self.tail_ptr = (self.tail_ptr + 1) % self.queue_size
		self.size += 1

	def dequeue(self):
		if self.current_size == 0:
			raise 'Queue is empty'
			return
		value = self.queue[head_ptr]
		self.head_ptr = (self.head_ptr + 1) % self.queue_size
		self.current_size -= 1
		return value

	def get_size(self):
		return self.current_size
