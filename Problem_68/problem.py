# Simple implementation, improvement could be done by groupings.
def solve(bishops, m):
	def attacked(b1, b2):
		return abs(b2[0] - b1[0]) == abs(b2[1] - b1[1])

	count = 0
	for idx, bishop in enumerate(bishops):
		for sub_bish in bishops[i + 1:]
			count += 1 if attacked(bishop, sub_bish) else 0
	return count
		
