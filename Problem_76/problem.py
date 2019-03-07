def reduce(arr):
	if arr is None:
		return arr

	'''
		cba
		daf
		ghi
	
		ca
		df
		gi
		1

		abcdef
		0

		Brute force Time O(n*m)
	'''
	removes = 0
	for col in range(len(arr[0])):
		prev = 0
		for row in range(len(arr)):
			if prev > ord(arr[row][col]):
				removes += 1
				break
			prev = ord(arr[row][col])
	return removes

arr = [['c','b','a'],['d','a','f'],['g','h','i']]
print(reduce(arr))

arr = [['a','b','c','d','e','f','g','h']]
print(reduce(arr))

arr = [['z','y','x'],['w','v','u']]
print(reduce(arr))
