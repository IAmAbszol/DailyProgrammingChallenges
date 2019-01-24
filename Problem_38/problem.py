solutions = 0
def solve(n):
	if n < 1:
		return n
	
	# Construct board
	board = [['.' for i in range(n)] for j in range(n)]

	def display(row):
		print(row)
		for r in board:
			print(r)

	def helper(row):
		if row >= n:
			return 1
		
		for i in range(n):
			board[row][i] = 'Q'
			display(row)
			if is_safe(row + 1):
				helper(row + 1)
			board[row][i] = '.'			
	
	def is_safe(queens):
		rows = set()
		cols = set()
		northEast = set()
		southEast = set()
		for row in range(n):
			for col in range(n):
				if board[row][col] == 'Q':
					rows.add(row)
					cols.add(col)
					northEast.add(row + col)
					southEast.add(n - 1 - row + col)
		total = queens - len(rows)
		total += queens - len(cols)
		total += queens - len(northEast)
		total += queens - len(southEast)
		return False if total else True
	
	helper(0)
	return solutions

print(solve(8))



