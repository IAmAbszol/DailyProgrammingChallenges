'''
	Go through each move and corresponding location.
	Contain a queue of (current, turns).
	Using breadth will reveal the first location.
	Contain a visited portion as well to contain if it visited, if not, update, add move and turn + 1 to queue.
	
	Book solution as it makes the most sense.

'''

from collections import deque

def minimum_moves(snakes, ladders):
	board = {square: square for square in range(1, 101)}

	# Change board locations if on square, where does it go.
	for start, end in snakes.items():
		board[start] = end

	for start,end in ladders.items():
		board[start] = end

	start, end = 0, 100
	turns = 0

	# Path we've traversed so far with current position and turns
	path = deque([(start, turns)])
	visited = set()

	while path:

		square, turns = path.popleft()

		for move in range(square + , square + 6):
			if move >= end:
				return turns + 1

			if move not in visited:
				visited.add(move)
				path.append((board[move], turns + 1))


	
