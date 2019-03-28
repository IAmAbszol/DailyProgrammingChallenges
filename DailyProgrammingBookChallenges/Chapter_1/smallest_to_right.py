import bisect

# Adapted solution, page 27. Never used bisect before =D
'''
	Explaining the wizardry
	... Bisect allows an insertion of nlog(n), n is originally separate till placement.
		Each index acts as, how many are we ahead. Hence on the rev list
		1 6 9 4 3
		1 is 0, idx 0
		6 is 1
		9 is 2
		When were at 4, we place it after 1, hence 1
		When were at 3, we place it after 1, hence 1
		Reverse that, we get 1 1 2 1 0
'''
def smallest(arr):
	if arr is None:
		return arr

	result = []
	seen = []
	for elm in reversed(arr):
		idx = bisect.bisect_left(seen, elm)
		result.append(idx)
		print(seen, result)
		bisect.insort(seen, elm)
	return list(reversed(result))

print(smallest([3,4,9,6,1]))
