'''
	Books solution is actually the best.

		1,2,5,4,3,6
Left        ^
Right	        ^
'''

import sys

def problem(arr):
	
	left, right = 0, 0
	minimum = sys.maxsize
	maximum = -sys.maxsize

	for i in range(len(arr)):
		maximum = max(maximum, arr[i])
		if arr[i] < maximum:
			right = i

	for i in range(len(arr) - 1, -1, -1):
		minimum = min(minimum, arr[i])
		if arr[i] > minimum:
			left = i

	return left, right

print(problem([1,2,5,4,3,6]))
