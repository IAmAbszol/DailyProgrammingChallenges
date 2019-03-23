'''
	Find the min and max of an array efficiently
'''

# Common approach
def common(arr):
	if arr is None:
		return None

	min_int, max_int = arr[0], arr[0]
	compare = lambda x, y : (x,y) if y > x else (y,x)

	# If we make this odd, the remaining comparisons are neater.
	if len(arr) % 2 == 0:
		arr.append(arr[-1]) 

	for i in range(1, len(arr), 2):
		smaller, bigger = compare(arr[i], arr[i + 1])
		min_int = min(smaller, min_int)
		max_int = max(bigger, max_int)
	return min_int, max_int

# Recursive approach
def recursive(arr):
	
	# Base case, what if len == 1
	if len(arr) == 1:
		return arr[0], arr[0]
	elif len(arr) == 2:
		return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
	else:
		n = len(arr) // 2
		l_min, l_max = recursive(arr[:n])
		r_min, r_max = recursive(arr[n:])
		return min(l_min, r_min), max(l_max, r_max)
