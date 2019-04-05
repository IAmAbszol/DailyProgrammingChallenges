'''
	This problem is actually the RGB problem.
	We can compare constantly with mid
	to store R-G-B inside their respective partitions.

	1. If mid is the lower, swap with lower and increment both.
	2. If mid is then regular, increment.
	3. Remainder: Swap mid with high. Decrement high.
'''

def sort(arr):
	low = mid = 0
	high = len(arr) - 1
	while mid <= high:
		if arr[mid] == 0:
			arr[low], arr[mid] = arr[mid], arr[low]
			low += 1
			mid += 1
		elif arr[mid] == 1:
			mid += 1
		else:
			arr[mid], arr[high] = arr[high], arr[low]
			high -= 1
	return arr	
print(sort([2,0,2,1,1,0]))
