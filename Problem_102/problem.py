'''
	1,2,3,4,5 sum = 9

	      ^
	  ^
	9
'''
# Bounding problem when right += 1 occurs, then accesses list.
def problem(arr, k):

	if arr is None:
		return arr

	if k < arr[0]:
		return None

	left = 0
	right = 0
	# Since 1,1 is not in the array, only a single.
	total_sum = arr[left]
	while left < len(arr) and right < len(arr):
		if total_sum == k:
			return arr[left:right + 1]
		# Move right up & add value.
		elif total_sum < k:
			right += 1
			total_sum += arr[right]
		# Decrement value && move left up.
		elif total_sum > k:
			total_sum -= arr[left]
			left += 1

print(problem([1,2,3,4,5],9))
