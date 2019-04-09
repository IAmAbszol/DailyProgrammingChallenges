'''
	[100, 4, 200, 1, 3, 2]

	Given this sequence, solve for the longest consecutive sub sequence (1,2,3,4).
	Must be in O(n) time.

	Thought 1: Calculate the offset needed to connect the two numbers together.
	Meaning given 4, we need 5 or 3, thus we want constant look up time, store these
	in a hash.

	hash[4] = [3,5]

	By the end, we should have a hash
	
	{
		100: 99, 101,
		4: 3, 5,
		200: 199, 201,
		1: 0, 2,
		3: 2, 4,
		2: 1, 3
	}
	So now we go through by sorting the hashes keys and pretty much hop.
	Problem, it's not O(n).

	Another way is to check if it's in the hash, if it is, calculate the max distance.

	Ex.

	When 3 is introduced

	hash {
		4 : 3, 5
		1 : 0, 2
		3 : 2, 4
	}
	Take 3 as base start (Assume its absolute least). 
	Is 4 in the hash? Yes, increase longest.

	When 2 finally gets placed.

	Adjustment, check if left is in hash, if so, iterate, if not, iterate from
	current.

	Is 1 in hash? Yes, is 2? Yes, is 3? Yes, is 4? Yes.

	Longest is 4.

	Lets make it faster. As we build, check if left and right is in the hash, if so, adjust to there left and right. In the end, we will have a massively connected network.
'''

def problem(arr):

	d = {}
	longest = 0
	for i in arr:
		left, right = i, i
		# Check if left most side is in the hash, if so, link.
		if left - 1 in d:
			left = d[left - 1][0]
		if right + 1 in d:
			right = d[right + 1][1]

		d[left] = left, right
		d[right] = left, right
		d[i] = left, right

		longest = max(longest, right - left + 1)
	return longest

print(problem([100, 4, 200, 1, 3, 2]))
