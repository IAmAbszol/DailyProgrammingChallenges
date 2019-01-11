'''
	solution.py
	Decided to do this in Python, since it appeals
	to perform list/array manipulation in Python 
	rather than Java.
'''

import unittest

def solve(islands):

	def dfs(row, col, islands):
		if row < 0 or row >= len(visited):
			return
		if col < 0 or col >= len(visited[row]):
			return
		if islands[row][col] == 1 and not visited[row][col]:
			visited[row][col] = True
		else:
			return
		# Start from center to left, go clock wise
		dfs(row, col - 1, islands)
		dfs(row - 1, col - 1, islands)
		dfs(row - 1, col, islands)
		dfs(row - 1, col + 1, islands)
		dfs(row, col + 1, islands)
		dfs(row + 1, col + 1, islands)
		dfs(row + 1, col, islands)
		dfs(row + 1, col - 1, islands)
		return	

	count = 0
	visited = [[False for i in islands[j]] for j in range(len(islands))]
	for row in range(len(islands)):
		for col in range(len(islands[row])):
			if islands[row][col] == 1 and not visited[row][col]:
				count += 1
				dfs(row, col, islands)
	return count


class Test(unittest.TestCase):
	
	island = [[0,0,0,0,0,0,0,0,0,0],[1,1,0,0,1,1,0,0,1,0],[1,1,1,0,0,1,0,0,1,1],[0,1,0,0,0,1,0,1,0,1]]
	data = [(island, 3)]
	
	
	def test_solution(self):
		for [case, expected] in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
