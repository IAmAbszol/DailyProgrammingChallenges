import unittest

from copy import deepcopy

def is_valid_move(board, px, py):
	return 0 <= py < len(board) and 0 <= px < len(board[0]) and not board[py][px]

def next_moves(board, px, py):
	move_sublist = [
	(2, 1),
	(1, 2),
	(1, -2),
	(-2, 1),
	(-1, 2),
	(2, -1),
	(-1, -2),
	(-2, -1),
	]
	
	moves = [(py + y_delta, px + c_delta) for y_delta, c_delta in move_sublist]
	return  [move for move in moves if is_valid_move(board, move[0], move[1])]


def solve(n):
	if n < 1:
		return None
	count = 0
	for i in range(n):
		for j in range(n):
			board = [[False for _ in range(n)] for _ in range(n)]
			board[i][j] = True
			count += helper(deepcopy(board), [(i, j)], n)
	return count
	

def helper(board, tour, n):
	if len(tour) == n * n:
		return 1
	else:
		count = 0
		previous_r, previous_c = tour[-1]
		for r, c in next_moves(board, previous_c, previous_r):
			tour.append((r, c))
			board[r][c] = True
			count += helper(deepcopy(board), tour, n)
			tour.pop()
			board[r][c] = False
		return count

print(solve(3))
