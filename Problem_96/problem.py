def permutations(arr, l, r):
	if l == r:
		print(arr)
		return

	def swap(arr, a, b):
		arr[a], arr[b] = arr[b], arr[a]

	for i in range(l, r + 1):
		swap(arr, l, i)
		permutations(arr, l + 1, r)
		swap(arr, l, i)

permutations([1,2,3], 0, 2)
		
