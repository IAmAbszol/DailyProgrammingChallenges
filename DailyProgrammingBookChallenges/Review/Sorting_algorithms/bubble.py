def bubble(arr):
	if arr is None:
		return arr
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		for i in range(1, len(arr)):
			if arr[i] < arr[i - 1]:
				arr[i], arr[i - 1] = arr[i - 1], arr[i]
				is_sorted = False
	return arr

array = [5,1,4,2,8]
print(bubble(array))

