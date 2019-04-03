'''
	3 4 9 1 2
	[ 2 2 2 0 0]

	0 0 2 2 2  --> reverse
'''

import bisect

def problem(arr):
	result = []
	seen = []
	for i in reversed(arr):
		idx = bisect.bisect_left(seen, i)
		result.append(idx)
		bisect.insort(seen, i)
	return list(reversed(result))

print(problem([3,4,9,1,2]))
