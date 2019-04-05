'''
	1,2
	1,3
	1,4
	2,3
	2,4
	3,4

	list = []
	for i in n + 1
		sub append i
		backtrack(n, k, i + 1, sub)	 --> start on i + 1 as we can't have dupes.
		sub remove last
'''
from copy import deepcopy

result = []
def problem(n, k, s, sub):
	if len(sub) == k:
		result.append(deepcopy(sub))
		return
	for i in range(s, n + 1, 1):
		sub.append(i)
		problem(n, k, i + 1, sub)
		sub.pop()

problem(4, 2, 1, [])
print(result)
