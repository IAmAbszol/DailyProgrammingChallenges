'''
	5,1,2,3,4	l > m < h	Case 2
	4,5,1,2,3	l > m < h
	1,2,3,4,5	l < m < h	Case 1
	3,4,5,1,2	l < m > h	Case 3
	2,3,4,5,1	l < m > h
'''
def problem(arr, k):
	left = 0
	right = len(arr) - 1
	while left <= right:
		mid = (left + right) / 2
		if arr[mid] == k:
			return True
		if arr[left] < arr[mid]:
			if arr[left] <= k and k < arr[mid]:
				right = mid - 1
			else:
				left = mid + 1
		elif arr[left] > arr[mid]:
			if arr[mid] < k and k <= arr[right]:
				left = mid + 1
			else:
				right = mid - 1
		# Add onto the original search. Move left up to move past dupes.
		else:
			while left < right and arr[left] == arr[right]:
				left += 1
			if left < mid:
				continue
			else:
				left = mid + 1
	return False
