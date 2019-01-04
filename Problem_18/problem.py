def find_maxes(array, k):
	if k > len(array):
		yield -1
		return
	start = 0
	end = k
	while end <= len(array):
		yield max(array[start:end])
		start += 1
		end += 1


print([i for i in find_maxes([10,5,2,7,8,7], 3)])
