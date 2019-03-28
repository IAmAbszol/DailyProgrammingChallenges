'''
	Progressive linking
	This works as 4 is the highest, right side dne.
	When we get to 3, we say look for 4, oh it exists. Take 4s bounds because maybe theres something higher.
	When were on 2, we check the left and say, oh look theres a 1, take 1's lower bound. This will be 1.
	Hence when were finally at 2, we should have left = 1, right is 4 since 3 was mapped to 4.

	If we were to expand further

	6,5,4,3,2,1.
	Stepping through
	6 -> (6,6)
	5 -> (5,6)
	4 -> (4,6)
	3 -> (3,6)
	...

	1,2,3,4,5,6.
	1 -> (1,1)
	2 -> (1,2)
	...
	
	It works.

	Another two strategies are either sorting for O(nlog(n)) as we would just traverse and find the longest running (arr[i] > arr[i - 1])
	The other would be close to what were using.
	Preprocess all elements inside a set. Check if arr[i] + 1 is within the set, if so, traverse from j = arr[i] + 1 till its none.
	Take the index we started being i and subtract the difference from j. That will be our current longest.
'''

def longest(arr):

	longest = 0
	bounds = {}

	for element in arr:
		
		left, right = element, element
		# Branch, build off of left and right
		if left - 1 in bounds:
			left = bounds[left - 1][0]
		if right + 1 in bounds:
			right  = bounds[right + 1][1]
		bounds[left] = left, right
		bounds[element] = left, right
		bounds[right] = left, right
		longest = max(longest, right - left + 1)

	return longest

print(longest([100, 4, 200, 1, 3, 2]))
