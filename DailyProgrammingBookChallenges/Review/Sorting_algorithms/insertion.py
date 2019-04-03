def insertion(arr):
	if arr is None:
		return arr
	for i in range(1, len(arr)):
		ptr = arr[i]
		sub = i - 1
		while sub >= 0 and ptr < arr[sub]:
			arr[sub + 1] = arr[sub]
			sub -= 1
		arr[sub + 1] = ptr
	return arr

print(insertion([5,4,3,2,1]))
