def plus_one(arr):
	carry = 0
	arr[-1] += 1
	for i in range(len(arr) - 1, -1, -1):
		arr[i] += carry
		if arr[i] > 9:
			arr[i] = 0
			carry = 1
		else:
			carry = 0
			break
	if carry:
		arr.insert(0, 1)
	return arr

print(plus_one([1,2,3]))
print(plus_one([1,2,9]))
print(plus_one([1,2,0]))
print(plus_one([9,9]))
