def organize(arr):
	if arr is None:
		return arr
	low = 0
	mid = 0
	high = len(arr) - 1
	while mid <= high:
		if arr[mid] == 'R':
			arr[low], arr[mid] = arr[mid], arr[low]
			low += 1
			mid += 1
		elif arr[mid] == 'G':
			mid += 1
		else:
			arr[mid], arr[high] = arr[high], arr[mid]
			high -= 1
	return arr			

print(organize(['B','G','B','B','G','R','B','R']))
