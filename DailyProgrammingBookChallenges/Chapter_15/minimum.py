'''
	We want to do this problem faster than O(n), we can do it in worst case of O(log(n)) time
	This problem can be done by using a binary-search implementation.
'''

def binary_rotated(arr, key):
	if arr is None:
		return arr
	low = 0
	high = len(arr) - 1
	
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == key:
			return mid

		if arr[low] <= arr[mid]:
			if key >= arr[low] and key <= arr[mid]:
				high = mid - 1
			else:
				low = mid + 1
		else:
			if key >= arr[mid] and key <= arr[high]:
				low = mid + 1
			else:
				high = mid - 1

print(binary_rotated([4,1,2,3], 4))
