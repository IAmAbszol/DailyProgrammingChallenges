def binary_ceil(arr, val):
	if not arr:
		return None
	low = 0
	high = len(arr) - 1
	ceil = None
	while low <= high:
		mid = int((low + high) / 2)
		if arr[mid] == val:
			return val
		if val < arr[mid]:
			ceil = arr[mid]
			high = mid - 1
		else:
			low = mid + 1
	return ceil

def binary_floor_ceil(arr, val):
	if not arr:
		return None
	low = 0
	high = len(arr) - 1
	floor = None
	ceil = None
	while low <= high:
		mid = int((low + high) / 2)
		if arr[mid] == val:
			return val
		if val < arr[mid]:
			ceil = arr[mid]
			high = mid - 1
		else:
			floor = arr[mid]
			low = mid + 1
	return floor, ceil

arr = [ 1, 2, 8, 10, 10, 12, 19 ]
print(binary_floor_ceil(arr, 0))
print(binary_floor_ceil(arr, 1))
print(binary_floor_ceil(arr, 5))
print(binary_floor_ceil(arr, 20))
