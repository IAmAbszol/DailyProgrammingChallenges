'''
	A simple problem
	10 5 7, we want an increasing list of integers but can only change at most 1 element.
	Proposition
	Scan the list
	if prev > cur
		change prev, set change counter to 1.
	By the end, if change counter > 1, return false else true

'''

import sys

def solution(arr):
	if arr is None:
		return arr
	counter = 0
	prev = -sys.maxsize
	for elm in arr:
		if prev > elm:
			counter += 1
		prev = elm
	return True if counter <= 1 else False

print(solution([10,5,1]))
print(solution([10,5,7]))
