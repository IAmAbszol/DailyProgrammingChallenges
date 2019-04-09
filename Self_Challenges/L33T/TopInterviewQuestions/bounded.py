'''
	x x x x
	x o o x
	x x o x
	x o x x

	Island problem comes to mind when solving
	Any 0, check for x. if out of bounds, any traversed region is then marked with ?.

	Problem: That's a lot but theres a base case, o on the border and any connecting isn't
	bounded by x. Thus traverse the outskirts till o, then dfs and place ? markers.

	Retraverse the board, any o's become x's and any ?'s become o's.

	Profit.
'''

def problem(board):

	# Traverse the board
	def dfs(board, i, j):
		if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == 'x':
			return
		board[i][j] = '?'
		for y, x in [(1,0),(0,1),(-1,0),(0,-1)]:
			dfs(board, i + y, j + x)

	# Traverse the boundaries
	for parallel in range(0, len(board[0])):
		if board[0][parallel] == 'o':
			dfs(board, 0, parallel)
		elif board[len(board) - 1][parallel] == 'o':
			dfs(board, len(board) - 1, parallel)

	for perpendicular in range(0, len(board)):
		if board[perpendicular][0] == 'o':
			dfs(board, perpendicular, 0)
		elif board[perpendicular][len(board[0]) - 1] == 'o':
			dfs(board, perpendicular, len(board[0]) - 1)
	
	# Swap up
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 'o':
				board[i][j] = 'x'
			elif board[i][j] == '?':
				board[i][j] = 'o'

	return board

print(problem([['x','x','x','x'],['x','o','o','x'],['x','x','o','x'],['x','o','x','x']]))
