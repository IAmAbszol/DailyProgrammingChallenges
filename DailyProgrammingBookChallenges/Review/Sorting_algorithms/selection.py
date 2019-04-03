import sys

def selection(arr):
	if arr is None:
		return arr
	def smallest(arr):
		element = sys.maxsize
		idx = 0
		for i in range(len(arr)):
			if arr[i] < element:
				element = arr[i]
				idx = i
		return element, idx
	left_ptr = 0
	while left_ptr < len(arr):
		element, idx = smallest(arr[left_ptr:])
		arr[left_ptr], arr[idx + left_ptr] = arr[idx + left_ptr], arr[left_ptr]
		left_ptr += 1
	return arr

array = [64,25,12,22,11]
print(selection(array))
