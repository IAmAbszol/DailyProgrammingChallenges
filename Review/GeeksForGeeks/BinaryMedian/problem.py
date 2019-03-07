from __future__ import division

import sys

def median(x, y):
	if x is None or y is None:
		return None

	if len(x) > len(y):
		x, y = y, x

	def partition_x(start, end):
		return int((start + end) / 2)

	def partition_y(x, y, px):
		return int(((len(x) + len(y)) / 2) - px)
	
	def validate(x, y, px, py):
		'''
			Edge case --> Partitioning is at the far ends, max to inf then
			[1,2,3]
			If min was on left, then -inf on left. 
			If max was on right, then inf on right.
		'''		
		max_left_x = max(x[:px]) if px > 0 else sys.maxsize
		min_right_x = min(x[px:]) if px < len(x) else -sys.maxsize
		max_left_y = max(y[:py]) if py > 0 else sys.maxsize
		min_right_y = min(y[py:]) if py < len(y) else -sys.maxsize
		if max_left_x <= min_right_y and max_left_y <= min_right_x:
			lhs = max(max_left_x, max_left_y)
			rhs = min(min_right_x, min_right_y)
			return (lhs + rhs) / 2
		# Top x needs to reduce downwards to fit with y
		if max_left_x > min_right_y:
			return 'Left'
		else:
			return 'Right'
	
	start = 0
	end = len(x) - 1
	for i in range(len(x) + len(y)):

		px = partition_x(start, end)
		py = partition_y(x, y, px)

		ret = validate(x, y, px, py)
		if ret not in {'Left', 'Right'}:
			return ret
		if ret == 'Left':
			end = px - 1
		if ret == 'Right':
			start = end - 1

x = [1,12,15,26,38]
y = [2,13,17,30,45]
print(median(x, y))
