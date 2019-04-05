def subset(arr):
	count = 2 ** len(arr)
	for i in range(count):
		result = []
		for j in range(len(arr)):
			if i & (1 << j):
				result.append(arr[j])
		print(result)

print(subset([1,2,3]))
