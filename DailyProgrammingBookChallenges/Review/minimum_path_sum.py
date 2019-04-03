def dp(board):
	m = len(board[0])
	n = len(board)
	subs = [[0 for i in range(m)] for i in range(n)]
	subs[0][0] = board[0][0]
	for i in range(1,m):
		subs[0][i] = board[0][i] + subs[0][i - 1]
	for i in range(1, n):
		subs[i][0] = board[i][0] + subs[i - 1][0]
	for i in range(1, n):
		for j in range(1, m):
			subs[i][j] = board[i][j] + min(subs[i - 1][j], subs[i][j - 1])
	return subs[n - 1][m -1]

board = [
			[ 1, 3, 1 ],
			[ 1, 5, 1 ],
			[ 4, 2, 1 ]
		]
print(dp(board))
