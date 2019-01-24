def powerset(arr):
	if arr is None:
		return arr
	count = 2 ** len(arr)
	for c in range(count):
		power = []
		for j in range(len(arr)):
			if c & (1 << j):
				power.append(arr[j])
		print(power)

print(powerset([1,2,3]))
