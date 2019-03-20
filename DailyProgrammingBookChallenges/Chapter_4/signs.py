def reconstruct(arr):
	if arr is None or not arr:
		return None

	answer = []
	n = len(arr) - 1
	stack = []

	for i in range(n):
		if arr[i + 1] == '-':
			stack.append(i)
		else:
			answer.append(i)
			while stack:
				answer.append(stack.pop())
	stack.append(n)
	while stack:
		answer.append(stack.pop())

	return answer

print(reconstruct([None, '+', '+', '-', '+']))
print(reconstruct([None, '+', '-', '-', '-']))
