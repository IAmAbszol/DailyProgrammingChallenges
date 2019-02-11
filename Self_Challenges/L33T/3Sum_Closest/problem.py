import sys

'''
	Complexities
	O(n^2) time
	O(m) space where m is <= len(arr)
'''
def solve(arr, k):
	if arr is None:
		return arr
	solution = None
	closest_k = sys.maxsize
	for i in range(len(arr) - 2):
		for j in range(i + 1, len(arr) - 1):
			k = j + 1
			while k < len(arr):
				summed = sum([arr[i], arr[j], arr[k]])
				if abs(summed - k) < closest_k:
					closest_k = summed
					solution = [arr[i], arr[j], arr[k]]
				k += 1
	return solution, closest_k


print(solve([-1,2,1,-4], 1))
