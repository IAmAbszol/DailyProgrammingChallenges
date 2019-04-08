def dp(board):
	m = len(board[0])
	n = len(board)
	subs = [[0 for i in range(m)] for i in range(n)]
	for i in range(m):
		if board[0][i] == 0:
			subs[0][i] = 1
		else:
			break
	for i in range(n):
		if board[i][0] == 0:
			subs[i][0] = 1
		else:
			break
	for i in range(1, n):
		for j in range(1, m):
			if board[i][j] == 0:
				subs[i][j] = subs[i - 1][j] + subs[i][j -1]
			else:
				subs[i][j] = 0
	return subs[n - 1][m -1]

board = [
			[ 0, 0, 0 ],
			[ 0, 1, 0 ],
			[ 0, 0, 0 ]
		]
print(dp(board))
