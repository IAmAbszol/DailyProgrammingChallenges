'''
	Houses, taking previous
	prev = row 0

	Start at row 1

	Check previous row and adjacent elements, grab the minimum.
	The only restriction like houses is that we can only use adjacent elements.

	This j - 1 and j.

	After that, its just adding the current value to the minimum of the previous row
	thats adjacent.
	
'''

def triangle(matrix):
	for i in range(1, len(matrix)):
		for j in range(len(matrix[i])):
			# Observe only previous adjacent values to this, though 
			# it still must be within the scope
			matrix[i][j] += min([matrix[i - 1][k] for k in (j - 1, j) if 0 <= k < len(matrix[i - 1])])
	return min(matrix[-1])

print(triangle([[2],[3,4],[6,5,7],[4,1,8,3]]))
