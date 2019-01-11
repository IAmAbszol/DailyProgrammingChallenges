'''
	solution.py
	Extremely similar to the island problem, 
	this time it's number of steps.
'''

import sys
import copy
import unittest

def solve(case):
	'''
		Takes in 3 parameters and constructs 
		a map in order to find the shortest path.
		
		Parameters
		case : Tuple
				my_map : 2-D map of booleans, False you can walk, True you cannot.
				start : Starting position on the grid.
				end : Ending position or goal.	

		Returns
		steps : Number of minimum steps garnered

	'''
	my_map = case[0]
	start = case[1]
	end = case[2]
	visited = copy.deepcopy(my_map)

	steps = helper(my_map, visited, start, end, 0)
	return steps

# Deep copy was important, modifying callers visited, hence acted
# as a global visited rather than local. Whoops.
def helper(my_map, visited, start, end, steps):
	x, y = start
	if start == end:
		return steps
	if x < 0 or x >= len(my_map[0]):
		return sys.maxsize
	if y < 0 or y >= len(my_map):
		return sys.maxsize
	if visited[x][y]:
		return sys.maxsize

	steps += 1
	visited[x][y] = True
	# Following U, D, L, R
	steps = min(helper(my_map, copy.deepcopy(visited), (x - 1, y), end, steps), 
				helper(my_map, copy.deepcopy(visited), (x + 1, y), end, steps),
				helper(my_map, copy.deepcopy(visited), (x, y - 1), end, steps),
				helper(my_map, copy.deepcopy(visited), (x, y + 1), end, steps))
	return steps

class Test(unittest.TestCase):
	
	data = [(([[False, False, False, False],[True, True, False, True], [False, False, False, False], [False, False, False, False]],(3,0), (0,0)), 7)]
	
	
	def test_solution(self):
		for [case, expected] in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
