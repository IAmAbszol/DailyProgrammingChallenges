import sys
import unittest

class Stack:

	def __init__(self):
		self.stack_list = []

	def push(self, element):
		self.stack_list.append(element)

	def pop(self):
		return self.stack_list.pop()

	def max_element(self):
		return max(self.stack_list)

def solve(arr):

	if arr is None:
		return arr
	
	stack = Stack()
	for elm in arr:
		stack.push(elm)

	return (stack.pop(), stack.max_element())
			


class Test(unittest.TestCase):
	
	data = [([10, 12, 4, 5, 1, 0, 19], (19, 12))]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
