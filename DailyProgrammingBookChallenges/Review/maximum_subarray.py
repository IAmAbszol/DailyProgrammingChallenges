def maximum(arr):
	return kadanes(arr), divide(arr, 0, len(arr) - 1)

def kadanes(arr):
	curr = 0
	total = 0
	for i in range(len(arr)):
		curr = max(arr[i], curr + arr[i])
		total = max(curr, total)
	return total

def divide(arr, i, j):
	if i == j:
		return arr[i]
	mid = (i + j) // 2
	# Collect left and right positions
	left_res = divide(arr, i, mid)
	right_res = divide(arr, mid + 1, j)

	# Iterate through i to mid and find running max.
	left = leftMax = arr[mid]
	for i in range(i - 1, mid - 1):
		left += arr[i]
		leftMax = max(left, leftMax)

	# Same with right
	right = rightMax = arr[mid + 1]
	for i in range(mid + 2, j + 1):
		right += arr[i]
		rightMax = max(right, rightMax)
	# What about if left crosses with right?
	combined = leftMax + rightMax

	# Return absolute
	return max(combined, left_res, right_res)

print(maximum([-2,1,-3,4,-1,2,1,-5,4]))
