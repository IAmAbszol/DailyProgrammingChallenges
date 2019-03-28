'''
	Reattempting this problem

	I'll use the example as a base line build
	Letters are prioritized as RGB

	G, B, R, R, B, R, G
	
	Set low, mid, high
	* Originally checked if low is R. This actually isn't needed as low = mid off the rip.
	If mid is R, swap with low, update R, mid
	If mid is G, update mid
	Else
		swap mid, high,
		update both

'''

def organize(arr):
	if arr is None:
		return arr
	low = 0
	mid = 0
	high = len(arr) - 1
	while mid <= high:
		if arr[mid] == 'R':
			arr[low], arr[mid] = arr[mid], arr[low]
			mid += 1
			low += 1
		elif arr[mid] == 'G':
			mid += 1
		else:
			arr[mid], arr[high] = arr[high], arr[mid]
			high -= 1
	return arr
