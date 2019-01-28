import unittest
import sys

def solve(case):
	
	def compute_partition_x(start, end):
		return int((start + end) / 2)

	def compute_partition_y(x, y, partition_x):
		return int((len(x) + len(y) + 1) / 2) - partition_x

	def validate_partitions(x, y, partition_x, partition_y):
		# Check len(x) param, might need to be len(x) - 1
		maxLeftX = max(x[:partition_x]) if partition_x > 0 else -sys.maxsize
		minRightX = min(x[partition_x:]) if partition_x < (len(x)) else sys.maxsize
		maxLeftY = max(y[:partition_y]) if partition_y > 0 else -sys.maxsize
		minRightY = min(y[partition_y:]) if partition_y < (len(y)) else sys.maxsize

		if maxLeftX <= minRightY and maxLeftY <= minRightX:
			return ((max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2)
		elif maxLeftX > minRightY:
			# Move to the left 
			return  'Left'

		else:
			return 'Right'

	x = case[0]
	y = case[1]
	if x is None or y is None:
		return None
	
	if len(x) > len(y):
		x, y = y, x
	
	start = 0
	end = len(x) - 1
	# Time complexity should finish within log(n), hence run loop for n.
	for i in range(len(x) + len(y)):
		
		partition_x = compute_partition_x(start, end)
		partition_y = compute_partition_y(x, y, partition_x)
		
		ret = validate_partitions(x, y, partition_x, partition_y)
		# Found median
		if not ret is 'Left' and not ret is 'Right':
			return ret
		
		if ret is 'Left':
			end = partition_x - 1
		else:
			start = end - 1
	return None
			

class Test(unittest.TestCase):

	data = [(([1, 10, 18, 22],[3, 5, 8, 15, 19, 25]), 12.5),
			(([23, 26, 31, 35],[3, 5, 7, 9, 11, 16]), 13.5)]
	
	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
