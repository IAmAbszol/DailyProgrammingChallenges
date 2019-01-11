input = [i for i in range(9)]

def reverse(arr):
	for i in range(int(len(arr)/2)):
		tmp = arr[i]
		arr[i] = arr[len(arr) - i - 1]
		arr[len(arr) - i - 1] = tmp
	return arr

print(input)
print(reverse(input))
