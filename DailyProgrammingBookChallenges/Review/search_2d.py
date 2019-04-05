def search_2d(matrix, k):
	if k < matrix[0][0]:
		return False
	r, c = 0, 0
	for r in range(len(matrix)):
		if k < matrix[r][0]:
			r -= 1
			break
	while c < len(matrix[r]):
		if matrix[r][c] == k:
			return True
		c += 1
	return False

print(search_2d([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)) 
print(search_2d([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13)) 
		
