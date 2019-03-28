'''
	1 2 3
	[6, 3, 2]

	O(n^2) time.

	[1,2,3]
	
	[1,	2, 2]
	[,1

'''

def problem(arr):

	'''
		1,	2,	3
		1,	1,	2
		6,	3,	1
		6	3	2
	'''

	below = []
	above = []
	products = []

	p = 1
	for i in range(len(arr)):
		below.append(p)
		p *= arr[i]

	p = 1
	for i in range(len(arr) - 1, -1, -1):
		above.append(p)
		p *= arr[i]
	above = above[::-1]

	for i in range(len(arr)):
		products.append(below[i] * above[i])

	return products
	
print(problem([1,2,3]))
