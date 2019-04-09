'''
	3,1,5,8
	
	Playing, choose the maximum yield:
		Setup: Choosing ith balloon will yield coins
		nums[i - 1] * i * nums[i + 1]
		
		Nums < 0 or greater than >= n are 1.

	1 --> 15 coins
	
	3,5,8
	
	Burst 5 --> 120 + 15

	3, 8
	3 --> 24 + 120 + 15 + 8 (leftover) = 167

	Algorithm
	We need to evaluate all choices optimally, we could easily compute ALL possibilities
	within a range but that'd be insufficent.

	This algorithm is also not greedy, thus why all possibilities must be considered.

	A greedy strategy would occur at 3, 8, we would log 3 first as 3 * 8 and  8 * 3 are
	equal but later in the tree, 8 becomes the more optimal choice.

									3,1,5,8
	
				1,5,8				    3,5,8			3,1,8			3,1,5
		 5,8	 1,8	 1,5	 5,8	 3,8	 3,5		1,8	3,8	3,1		1,5	3,5	3,1
		8	5	1	8	1	5	5	8	3	8	3	5

	Start off idea
	Create a recursion tree(stack) that will compute the maximum of each choice.

	Improvement, cache observation for memoization.
	Problem: Python doesn't allow lists to be keys for a hash --> Understandable.
	Suggestion: Hash the list into a unique code. Careful though, 1,2,3 might equal 3,2,1.
	Application: Hash by index.
'''		

def burst(nums):

	def compute(nums, i):
		left = right = 0
		if i - 1 < 0:
			left = 1
		else:
			left = nums[i - 1]
		if i + 1 >= len(nums):
			right = 1
		else:
			right = nums[i + 1]
		return nums[i] * left * right

	if len(nums) == 1:
		return nums[0]
	
	score = 0
	# Iterate through choices, make i simulate the choice made.
	for i in range(len(nums)):
		remaining = [n for idx, n in enumerate(nums) if idx != i]
		local = compute(nums, i) + burst(remaining)
		score = max(score, local)
	return score

print(burst([3,1,5,8]))
