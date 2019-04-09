def problem(arr):
	stack = [0]
	res = []
	for i in range(len(arr)):
		if arr[i] < arr[stack[-1]]:
			res.append(stack[-1])
			stack = [0]
		stack.append(i)
	return res

print(problem([1,2,1,3,5,6,4]))
