import unittest

def solve(n, m):
	count = 1
	board = []
	for i in range(n):
		sub = []
		for j in range(m):
			sub.append(count)
			count += 1
		board.append(sub)
	
	# Spiral
	undone = []
	'''
		1,2,3
		4,5,6
		7,8,9
	'''		

	row, col = 0, 0
	dirs = [(0,1),(1,0),(0,-1),(-1,0)]
	change = [(0,-1),(-1,0),(0,1),(1,0)]
	direction = 0	
	undone.append(board[row][col])
	board[row][col] = -1
	while not all([c == - 1 for r in board for c in r]):
		move = dirs[direction]
		row += move[0]
		col += move[1]
		if row < 0 or row >= n or col < 0 or col >= m or board[row][col] == -1:
			delta = change[direction]
			row += delta[0]
			col += delta[1]
			direction += 1
			if direction >= len(dirs):
				direction = 0
			continue
		undone.append(board[row][col])
		board[row][col] = -1
	return undone
	
class Test(unittest.TestCase):

	data = [((4,5), [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12])]	
	
	def test(self):
		for case, expected in self.data:
			actual = solve(case[0], case[1])
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
		
