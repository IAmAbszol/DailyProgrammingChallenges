'''
	Given a cost matrix, compute the minimum cost
	The cost matrix consists of an hxk schema where h is the number of houses
	and k is the number of colors.

	Adjacent houses cannot have the same colors next to one another.
'''

def houses(matrix):

	prev = matrix[0]
	for i in range(1, len(matrix)):
		curr = matrix[i]
		for j in range(len(matrix[i])):
			curr[j] += min([v for idx, v in enumerate(prev) if idx != j])
		prev = curr
	print(prev)
	return min(prev)
