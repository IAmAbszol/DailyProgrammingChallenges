def next_permutation(arr):
	if arr is None:
		return arr

	def swap(arr, a, b):
		arr[a], arr[b] = arr[b], arr[a]

	def reverse(nums, a, b):
		nums[a:b+1] = reversed(nums[a:b+1])

	'''
		Solutions example 
		1. Start at the far right side, a base case of reason is if we had
		3 2 1, the next permutation would have to be 1,2,3 since no other permutation exists
		to make it greater than this.
			Starting at the far right side allows us to go to the next number up.
			Counting 123, we don't could 223 --> 124.

		2. Traverse the right until we hit the case that our previous number is less than our current. (Pivot point)
		3. Traverse the right until we hit the case that our current number is greater than our privot point.
		4. Swap the two values
		5. From our pivot point, move back one. Then reverse the whole list

		Ex: 123 --> Pivot is 2, 3 is our successor. Swap 132, move back one, swap 2, 2 --> 132
			132 --> Pivot is 1, 2 is our successor. Swap 1 and 2 --> 231, we know that the next part (Step 5) should definitely occur as
			our value of 231 > that what we need to produce.
			Step 5 --> swap pivot -1 --> 3 and 1 --> 213. Boom
			321 --> Pivot is -1 as we had no clear value. Hence we reverse the entire list.
	'''

	pivot = len(arr) - 2
	while arr[pivot] >= arr[pivot + 1] and pivot >= 0:
		pivot -= 1

	if pivot >= 0:

		turn = len(arr) - 1
		while nums[turn] <= nums[pivot] and turn > 0:
			turn -= 1
		swap(arr, pivot, turn)

	reverse(arr, pivot + 1, len(arr) - 1)
