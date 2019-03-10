import os
import sys

class Problem:

	def __init__(self):
		self.file_name = 'readme.txt'

	def read7(self, ptr=0):
		data = None
		with open(self.file_name, 'r') as f:
			data = f.read()[ptr:(ptr+7)]
			f.close()
		return data

	def readN(self, n):
		if n < 1:
			return None
		base = 10
		buffer = []
		ptr = 0
		while ptr < n:
			buffer.append(self.read7(ptr=ptr))
			ptr += 7
		return ''.join(buffer)[:n]
		
if __name__ == '__main__':
	problem = Problem()
	print(problem.readN(30))	