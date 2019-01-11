def search(array, left, right, target):
	if not array:
		return -1

	if left == right:
		return left if array[left] == target else -1

	mid = (left + right) / 2
	if array[mid] == target:
		return mid

	if array[left] <= array[mid]:
		if target >= array[left] and target <= array[mid]:
			return search(array, left, mid - 1, target)
		return search(array, mid + 1, right, target)

	if target >= array[mid] and target <= array[right]:
		return search(array, mid + 1, right, target)
	return search(array, left, mid - 1, target)


print(search([10, 12, 15, 1, 2, 6, 8], 0, 6, 6))
