import sys

class Stack:

	def __init__(self, stack_size=sys.maxsize):
		self.max_size = stack_size
		self.stack = []
		self.max_element = None

	def push(self, value):
		val = -sys.maxsize
		if len(self.stack) >= self.max_size:
			val = self.stack.pop()
		self.stack.append(value)		
		self.max_element = max(self.stack)
	
	def pop(self):
		value = self.stack.pop()
		if value == max_element:
			self.max_element = max(self.stack)
		return value

	def max_size(self):
		if not stack:
			raise ValueError('Empty stack!')
			return None
		return self.max_element
