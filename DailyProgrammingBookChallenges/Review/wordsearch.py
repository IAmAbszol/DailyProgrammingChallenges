def problem(board, word):
	'''
		DFS Solution
	'''
	def dfs(board, row, col, word, visited, pos):
		if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
			return False
		if (row, col) in visited:
			return False
		if board[row][col] != word[pos]:
			return False
		if pos == len(word) - 1:
			return True
		visited.add((row,col))
		for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
			if dfs(board, row + direction[0], col + direction[1], word, visited, pos + 1):
				return True
		visited.remove((row,col))

	for row in range(len(board)):
		for col in range(len(board[row])):
			visited = set()
			if dfs(board, row, col, word, visited, 0):
				return True
	return False

board = [
			[ 'A', 'B', 'C', 'E' ],
			[ 'S', 'F', 'C', 'S' ],
			[ 'A', 'D', 'E', 'E' ]
		]
print(problem(board, 'SEE'))
